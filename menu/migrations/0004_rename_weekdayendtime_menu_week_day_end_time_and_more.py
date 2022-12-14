# Generated by Django 4.1 on 2022-08-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_menu_days_menu_weekday_menu_weekdayendtime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='WeekDayEndTime',
            new_name='Week_Day_End_Time',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='WeekDayStartTime',
            new_name='Week_Day_Start_Time',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='WeekEndEndTime',
            new_name='Week_End_End_Time',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='WeekEndStartTime',
            new_name='Week_End_Start_Time',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='WeekDay',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='WeekEnd',
        ),
        migrations.AddField(
            model_name='menu',
            name='Week_Day',
            field=models.BooleanField(blank=True, default=False, help_text='Available on Weekdays?', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='Week_End',
            field=models.BooleanField(blank=True, default=False, help_text='Available on WeekEnds?', null=True),
        ),
    ]
