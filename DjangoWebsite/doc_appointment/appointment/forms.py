from django import forms
from .models import Appointment

hours=[
    ("9:00" , "9:00"),
    ("10:00" , "10:00"),
    ("11:00" , "11:00"),
    ("13:00" , "13:00"),
    ("14:00" , "14:00"),
    ("15:00" , "15:00"),
    ("16:00" , "16:00"),
]

class BookingForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form date'}))
    hour = forms.CharField(widget=forms.Select(choices=hours, attrs={'class':'form hour'}))
    more = forms.CharField(required = False, widget=forms.Textarea(attrs={'class':'form more'}))

