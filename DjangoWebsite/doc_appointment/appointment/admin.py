from django.contrib import admin


from appointment.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('booking_name', 'day', 'hour')

admin.site.register(Appointment, AppointmentAdmin)