# Generated by Django 4.2.5 on 2023-11-26 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_dept_description_departments_dep_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Booked_on',
            new_name='booked_on',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Booking_date',
            new_name='booking_date',
        ),
    ]
