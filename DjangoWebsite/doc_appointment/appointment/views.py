from django.shortcuts import render, redirect
from appointment.models import Appointment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def homepage(request):
    return render(request, 'appointment/homepage.html')

def appointment(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        messages.success(request, "Please login before booking an appointment")
        return HttpResponseRedirect(reverse("login")) #redirect to login page

    else:
        books = Appointment.objects.all()
        if request.method == 'POST':
            
            appointment = Appointment()
            appointment.day = request.POST['date']
            appointment.hour = request.POST['appt-time']
            appointment.booking_name = request.user.fullname
            appointment.save()
            
            messages.success(request, "appointment booked")

            return redirect('confirm')
        
        else:
            return render(request, 'appointment/appointment.html', {'books' : books})

def confirm(request):
    return render(request, 'appointment/confirm.html')
    