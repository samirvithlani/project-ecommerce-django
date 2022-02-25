from django import forms
from django.contrib.auth.models import User
from .models import *
from adminportal.product.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username', 'password','email','phone_number','profile_pic')

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ("username", "password", "email", "is_superuser", "is_staff", "is_active", "profile_pic", "phone_number",)

CHOICES = (
        ("H", "Home"),
        ("W", "Work"),
    )

class AddressForm(forms.ModelForm):
    user = forms.CharField(widget = forms.TextInput(attrs = {'name' : "user"}))
    address : forms.CharField(widget = forms.TextInput(attrs = {'name' : 'address'}))
    city_name : forms.CharField(widget = forms.TextInput(attrs = {'name' : "city_name"}))
    country_name : forms.CharField(widget = forms.TextInput(attrs = {'name' : "country_name"}))
    zip_code : forms.CharField(max_length=6,widget = forms.TextInput(attrs = {'name' : "zip_code"}))
    address_type =  forms.ChoiceField(choices=CHOICES)


    class Meta:
        model = Address
        fields = ("user",  "address", "city_name", "address_type", "country_name", "zip_code", )
        # widgets = {
        #             'address' : forms.Textarea(attrs = {'name' : 'address'}),
        #             'city_name' : forms.TextInput(attrs={'name' : 'city_name'}),
        #             'country_name' : forms.TextInput(attrs= {'name' : 'country_name'}),
        #             'zip_code' : forms.TextInput(attrs= {'name' : 'zip_code'}),
        #             'address_type' :  forms.RadioSelect(choices=[CHOICES])
        # }


# class UserProfileInfoForm(forms.ModelForm):
   
#     class Meta():
#         model = Customer
#         fields = ()
#         widgets = {}


