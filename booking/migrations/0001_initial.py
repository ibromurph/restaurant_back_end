# Generated by Django 4.1 on 2022-08-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingID', models.CharField(blank=True, max_length=12, null=True)),
                ('Booking_Time', models.TimeField()),
                ('Booking_Date', models.DateField()),
                ('Party_Size', models.IntegerField()),
                ('First_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Telephone_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('Type_of_Booking', models.BooleanField()),
                ('Get_Emails', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
