from django.db import models

# Create your models here.

class Appointment(models.Model):
    day = models.fields.DateField(auto_now=False, auto_now_add=False)
    hour = models.fields.TimeField(auto_now=False, auto_now_add=False)
    booking_name = models.fields.CharField(max_length=50)
    