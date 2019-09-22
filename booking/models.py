from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Userprofile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,
        primary_key=True,)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    about_us = models.CharField(max_length=100)
    


    def __str__(self):
        return self.full_name.title()

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = Userprofile.objects.create(User=kwargs['instance'])
post_save.connect(create_profile,sender=User)