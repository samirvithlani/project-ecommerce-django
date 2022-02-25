from pyexpat import model
from django.db import models
from generic.models import BaseField
from adminportal.user.models import *
from django.db.models.query_utils import Q

# Create your models here.
class Brand(BaseField):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Category(BaseField):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Product(BaseField):
    name = models.CharField(max_length=256)
    price = models.FloatField(null=False)
    detail = models.TextField()
    image = models.ImageField(upload_to="image/", default="image/p1.png" )
    brand = models.ForeignKey(Brand, related_name="product_brand", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class CartItem(BaseField):

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="cart_user")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="cart_product")
    quantity = models.IntegerField(default=0)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.product} for {self.user}"
        
    @property
    def get_cart_item(self):
        orderitem_1 = CartItem.objects.filter(Q(user__username = self.user))
        orderitem = list(orderitem_1)
        return orderitem

    @property
    def get_cart_total(self):
        total = self.product.price * int(self.quantity)
        return total

    @property
    def get_total(self):
        orderitems = self.get_cart_item
        total_1 = sum([items.get_cart_total for items in orderitems])    
        total = "%.2f" % (total_1 + float(0.18 * total_1))
        return total

class Address(BaseField):

    user_name = models.ForeignKey(User, null=True,  on_delete=models.CASCADE, related_name="user_name")
    address = models.CharField(max_length=256)
    address_type = models.CharField(max_length=10, default="Home")
    city_name = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)

    class Meta:
        db_table = "Addresses"

    def __str__(self):
        return f"{self.address_type} with {self.address}"

class Order(BaseField):

    cartitem = models.ForeignKey(CartItem, null=True,  on_delete=models.CASCADE, related_name="orderitem")
    address = models.ManyToManyField(Address, related_name="order_address")
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}-{self.get_purchased_display()}"

    @property
    def get_order_total(self):
        orderitems = self.cartitem_set.all()
        total = sum([items.get_cart_total for items in orderitems]) 
        # total = total_1 + int(0.18 * total_1)
        return total


# class ProductImage(BaseField):
#     product_id = models.ForeignKey(Product, verbose_name='parent_category', related_name='children',on_delete=models.CASCADE, default=0)
#     image = models.ImageField(upload_to="product/", default="product/p1.png" )

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url
