from django.db import models

class Appointment(models.Model):
    day = models.fields.DateField(auto_now=False, auto_now_add=False)
    hour = models.fields.CharField(max_length =5)
    more = models.fields.CharField(max_length = 200, blank = True)
    booking_user_id = models.fields.IntegerField()
    booking_name = models.fields.CharField(max_length=100, blank=True)
    happened = models.fields.BooleanField(default = False)
