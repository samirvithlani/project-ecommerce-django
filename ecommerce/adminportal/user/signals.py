from django.dispatch import receiver
from .models import *
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_user(sender, instance, created,  **kwargs):
    if created:
        user = instance.username
        print("New User have been created...", user)
    else:
        print("User have updated data..!!")