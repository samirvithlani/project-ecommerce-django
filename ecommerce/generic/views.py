from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from adminportal.user.forms import *
from adminportal.product.models import Product
from adminportal.product.forms import ProductAddForm
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login

# Create your views here.

#------------------------------User Base Class------------------------------------#

class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'userportal/registration.html'
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)  
        user.save()    
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " - User Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:login')

class BaseListView(LoginRequiredMixin, ListView):
    pass

class BaseDetailView(LoginRequiredMixin,DetailView):
    pass

class BaseAdminMixin(PermissionRequiredMixin):
    
    raise_exception = True
    permission_required = 'is_staff'
    redirect_field_name = 'next' 

    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name()) 

        if not self.has_permission():
            return redirect('/login-1/')
        return super(BaseAdminMixin, self).dispatch(request, *args ,**kwargs)

    '''def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to do this")
        return super(BaseAdminMixin, self).handle_no_permission()

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            path_redirect = request.get_full_path().split('?next=',1)
            print("------------------->>>", path_redirect)
            if '?next=' in request.get_full_path():# Redirecting After Login 
                print("<------- inside if")
                return redirect(path_redirect)
            else:
                print("><><><>< oiut side else")
                return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name()) 
        if not self.has_permission():
            return redirect('/login/')
        return super(BaseAdminMixin, self).dispatch(request, *args ,**kwargs)'''


#------------------------------Product Base Class------------------------------------#

class BaseCreateView(BaseAdminMixin, SuccessMessageMixin, CreateView, ListView):
    model = Product
    form_class = ProductAddForm
    template_name = "adminportal/product_creation.html"
 
    def get_success_message(self, cleaned_data):
        self.name = cleaned_data['name']
        return self.name + " Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class BaseUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductAddForm
    template_name = 'adminportal/update.html'
    # success_url = '/admin_customized/'

    def get_success_message(self, cleaned_data):
        self.name = cleaned_data["name"]
        return self.name + " Updated Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class BaseDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_message(self, cleaned_data):
        return "Product Deleted Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')




    
