# Generated by Django 4.1 on 2022-08-05 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_menu_day_delete_time_day_delete_weekdays_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu_Day',
            new_name='MenuDay',
        ),
        migrations.AlterModelOptions(
            name='menuday',
            options={'verbose_name_plural': 'Menu Day'},
        ),
    ]