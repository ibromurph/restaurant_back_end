# Generated by Django 4.1 on 2022-08-06 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_rename_lastname_tablebooking_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TableBooking',
        ),
    ]
