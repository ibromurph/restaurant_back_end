# Generated by Django 4.1 on 2022-08-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_tablebooking_bookingid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebooking',
            name='BookingID',
            field=models.CharField(blank=True, default='OuYLeeQcf7Sb', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='Get_Emails',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='Type_of_Booking',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]