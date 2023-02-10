from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('booking/', views.appointment, name='appointment'),
    path('confirm/', views.confirm, name ='confirm')
]