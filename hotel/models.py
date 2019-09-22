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
        verbose_name_plural = 'Room'

class Review(models.Model):
    image=models.FileField( upload_to='review/')
    name = models.CharField(max_length=30,default='name')
    customer = models.CharField(max_length=100 ,default='Satisfied Customer')
    description=models.TextField(max_length=1000)
    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name_plural = 'Review'

class feedback(models.Model):
    feedback_name = models.CharField(max_length=30,default='Name')
    feedback_email = models.CharField(max_length=30,default='E-mail')
    feedback = models.TextField(default='Feedback',max_length=500)
    def __str__(self):
        return self.feedback_name.title()

    class Meta:
        verbose_name_plural = 'feedback'



