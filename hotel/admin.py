from django.contrib import admin

# Register your models here.
from .models import Room,Review,feedback
admin.site.register(Room)
admin.site.register(Review)
admin.site.register(feedback)