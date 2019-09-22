from django.db import models

# Create your models here.
class Room(models.Model):
    image=models.ImageField( upload_to='rooms/')
    title = models.CharField(max_length=30,default='title')
    description = models.TextField(max_length=100 ,default='description')
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.title.title()

    class Meta:
        verbose_name_plural = 'room'
