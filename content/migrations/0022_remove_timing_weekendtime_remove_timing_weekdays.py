# Generated by Django 4.1 on 2022-08-08 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_carousel_imageopacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timing',
            name='WeekEndTime',
        ),
        migrations.RemoveField(
            model_name='timing',
            name='Weekdays',
        ),
    ]
