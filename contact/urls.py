from django.urls import path
from django.conf.urls import include, url
from .import views

urlpatterns = [
    path('contact/', views.contact, name="contact"),
]
