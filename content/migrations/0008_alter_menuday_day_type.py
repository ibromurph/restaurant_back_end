# Generated by Django 4.1 on 2022-08-05 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_rename_menu_day_menuday_alter_menuday_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuday',
            name='Day_Type',
            field=models.CharField(choices=[('WeekDays', 'WeekDays'), ('Weekend', 'Weekend')], max_length=300, unique=True),
        ),
    ]