# Generated by Django 4.1 on 2022-08-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_delete_homeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(upload_to='HomePageImg/')),
                ('Heading1', models.CharField(blank=True, max_length=100, null=True)),
                ('Paragraph', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'HomePage Image',
            },
        ),
    ]