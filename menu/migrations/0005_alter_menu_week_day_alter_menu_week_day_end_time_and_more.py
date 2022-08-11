# Generated by Django 4.1 on 2022-08-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_weekdayendtime_menu_week_day_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Week_Day',
            field=models.BooleanField(blank=True, default=False, help_text='Available on Week days?', null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Week_Day_End_Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Week_Day_Start_Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Week_End',
            field=models.BooleanField(blank=True, default=False, help_text='Available on Week Ends?', null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Week_End_End_Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Week_End_Start_Time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
