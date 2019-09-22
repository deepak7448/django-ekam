from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=30,default='Name')
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100 ,default='email')
    subjects = models.CharField(max_length=200 ,default='subject')
    messages = models.TextField(default='message')
    
    def __str__(self):
        return self.name.title()

