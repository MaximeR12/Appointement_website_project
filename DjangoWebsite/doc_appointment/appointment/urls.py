from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('booking/', views.appointment, name='appointment'),
    path('confirm/', views.confirm, name ='confirm'),
    path('profile/', views.profile, name ='profile'),
    path('appointment-list/', views.appt_list, name ='appt-list'),
    path('appointment-delete/<int:id>/', views.delete_appt, name ='appt-delete'),
    path("appointment-details/<int:id>/", views.details, name = 'details')
    
]