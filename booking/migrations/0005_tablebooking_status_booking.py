# Generated by Django 4.1 on 2022-08-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booktablecover2_text_alter_booktablecover2_cover_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebooking',
            name='Status_booking',
            field=models.CharField(blank=True, choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('EventPassed', 'EventPassed'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True),
        ),
    ]
