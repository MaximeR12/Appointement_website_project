# Generated by Django 4.1 on 2023-02-10 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_appointment_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='booking_name',
            new_name='booking_user_id',
        ),
    ]