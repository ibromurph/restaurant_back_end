# Generated by Django 4.1 on 2022-08-08 10:55

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_carousel_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='color',
            new_name='Color_Caption_Heading',
        ),
        migrations.AddField(
            model_name='carousel',
            name='Color_Caption_subHeading',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
    ]