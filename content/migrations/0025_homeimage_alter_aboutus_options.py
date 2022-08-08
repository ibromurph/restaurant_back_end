# Generated by Django 4.1 on 2022-08-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0024_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='HomeImage/')),
                ('Heading_one', models.CharField(max_length=100)),
                ('para', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Home Image',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
    ]