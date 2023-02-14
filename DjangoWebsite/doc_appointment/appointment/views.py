from django.shortcuts import render, redirect
from appointment.models import Appointment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import BookingForm
import datetime





def homepage(request):
    return render(request, 'appointment/homepage.html')


def appointment(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        messages.success(request, "Please login before booking an appointment")
        return HttpResponseRedirect(reverse("login")) #redirect to login page

    else:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():

                date=form.cleaned_data['date']
                hour=form.cleaned_data['hour']
                more=form.cleaned_data['more']

                if len(Appointment.objects.filter(day = date , hour = hour))>0: ################ VERIF SI DISPO
                    messages.success(request, "Please select another hour. The coach isn't free a the time you selected")
                    return render(request, 'appointment/appointment.html',{'form' : form})
                elif date < datetime.date.today():                              ################# VERIF SI DATE ANTERIEURE
                    messages.success(request, "Please select a date today / in the future")
                    return render(request, 'appointment/appointment.html',{'form' : form})
                elif date.weekday() >=5 :                                       ################# VERIF SI WEEKEND
                    messages.success(request, "The coach doesn't accept appointments on weekends")
                    return render(request, 'appointment/appointment.html',{'form' : form})    
                
                appointment = Appointment(
                day = date,
                hour = hour,
                more = more,
                )
                appointment.booking_user_id = request.user.id
                appointment.booking_name = request.user.first_name +' '+ request.user.last_name
                appointment.save()

                return redirect('confirm')  
        else:
            form = BookingForm()
    return render(request, 'appointment/appointment.html',{'form' : form})

def confirm(request):
    last_appointment = Appointment.objects.last()
    return render(request, 'appointment/confirm.html', {'appointment' : last_appointment, 'user' : request.user})
    

    

def appt_list(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        messages.success(request, "Please login to acces your bookings")
        return HttpResponseRedirect(reverse("login")) #redirect to login page
    else:
        bookings_incoming = []
        bookings_happened = []
        for appt in Appointment.objects.filter(booking_user_id = request.user.id):
            if not appt.happened:
                bookings_incoming.append(appt)
            else:
                bookings_happened.append(appt)
        return render(request, 'appointment/appt-list.html/',{'user' : request.user, "bookings_incoming" : bookings_incoming.sort(key= lambda x : x.day), 'bookings_happened' : bookings_happened.sort(key= lambda x : x.day), "nb_inc" : len(bookings_incoming), "nb_hap" : len(bookings_happened)} )
    

def delete_appt(request,id):
    appt = Appointment.objects.get(id = id)
    appt.delete()
    if request.user.is_staff:
        return redirect('planning')
    return redirect('http://127.0.0.1:8000/appointment-list/')


def details(request, id):
    appt = Appointment.objects.get(id = id)
    return render(request, 'appointment/details.html', {"appointment" : appt})

def profile(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        messages.success(request, "Please login")
        return HttpResponseRedirect(reverse("login")) #redirect to login page
    else:
        if request.method == 'POST':
            if request.POST["email"]:
                request.user.email = request.POST["email"]
            if request.POST['first_name']:
                request.user.first_name = request.POST['first_name']
            if request.POST["last_name"]:
                request.user.last_name = request.POST["last_name"]
            request.user.save()
            return render(request, 'appointment/profile.html/', {'user' : request.user})
        else:
            return render(request, 'appointment/profile.html/', {'user' : request.user})

def planning(request):
    bookings = Appointment.objects.all()
    if not request.user.is_staff: #if the user is a staff member
        messages.success(request, "You must be a staff user to access this page")
        return HttpResponseRedirect(reverse("login")) #redirect to login page
    else:
        return render(request, 'appointment/planning.html',{'bookings': bookings.order_by('day', 'hour')})