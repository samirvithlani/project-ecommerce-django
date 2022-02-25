from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# admin.site.register(User, UserAdmin)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "password", "email", "is_superuser", "is_staff", "is_active", "profile_pic", "phone_number", )
    list_display = ("username", "email", "is_staff")
    list_filter =  ("is_staff" , "created_at","updated_at",)

