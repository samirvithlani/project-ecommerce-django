
from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .views import *
from django.core.mail import send_mail

@shared_task
def checkout(user_id):
    print("user-id", user_id)
    user = User.objects.get(id = user_id)
    print("user------??", user)
    data = list()
    subtotal = 0
    cart_item = CartItem.objects.filter(user = user)
    # print ("cart_item", cart_item)
    for cart in cart_item:
        cart_dict = dict()
        # print("cart type", type(cart), cart)
        cart_dict["name"] = cart.product.name
        cart_dict["quantity"] = cart.quantity
        cart_dict["price"] = cart.product.price * cart.quantity
        subtotal = subtotal + cart_dict["price"]
        # print("subtotal", subtotal)
        cart.purchased = True
        
        cart.save()
        # print("CART-DICT inside for-------->>", cart_dict)
        data.append(cart_dict)
        # print(data)
    tax = subtotal * 0.18
    tax = "%.2f" % tax
    # print ( "TAX_____", tax)
    total = float(tax) + subtotal
    # print(total, "-------->> TOTAL")
    subject = "Thank you for the Shopping..!!"
    template_name = 'userportal/email.html'
    html_message = render_to_string(template_name, {"data":data, "subtotal": subtotal, "tax" : tax, "total" : total, "user" :user})
    plain_message = strip_tags(html_message)
    from_mail = settings.EMAIL_HOST_USER
    # print("from---mail", from_mail)
    to_mail = list()
    to_email = user.email
    to_mail.append(to_email)
    # print("to-------mail", to_mail)
    send_mail(subject, plain_message, from_mail, to_mail , html_message = html_message)

    