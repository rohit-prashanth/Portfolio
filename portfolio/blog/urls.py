from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.blog,name='blog'),
    path('bio', views.bio, name='bio'),
    path('edu', views.education, name='education'),
    path('contact', views.contact, name='contact'),
    path('thankyou',views.thankyou,name='thankyou')

]

