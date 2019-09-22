from django.urls import path
from django.conf.urls import include, url
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('room/', views.room, name="room"),
    path('facilities/', views.facilities, name="facilities"),
    #path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    
]
