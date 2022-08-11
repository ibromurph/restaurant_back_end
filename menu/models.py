from django.db import models
from colorfield.fields import ColorField
from backend.settings import CHOICES


class MenuCarousel(models.Model):
    Image = models.ImageField(upload_to='MenuCarousel/', help_text='Recommended Dimensions 2000x650')
    Caption_Heading = models.CharField(max_length=100)
    Caption_subHeading = models.CharField(max_length=100)
    ImageOpacity = models.IntegerField(null=True, blank=True, help_text='Enter in Percentage')
    Color_Caption_Heading = ColorField(default='#FF0000')
    Color_Caption_subHeading = ColorField(default='#FF0000')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Menu Carousel'


class MenuDay(models.Model):
    Day_Type = models.CharField(max_length=300, choices=CHOICES, blank=False, null=False, unique=True)
    Start_Time = models.TimeField()
    End_Time = models.TimeField()

    def __str__(self):
        return "{}-{}-{}".format(self.Day_Type, self.Start_Time, self.End_Time)

    class Meta:
        verbose_name_plural = 'Menu Day'


class Menu(models.Model):
    Title = models.CharField(max_length=100, null=True, blank=True)
    Week_Day = models.BooleanField(default=False, help_text='Available on Week days?', blank=True, null=True)
    Week_End = models.BooleanField(default=False, help_text='Available on Week Ends?', blank=True, null=True)
    Week_End_Start_Time = models.TimeField(blank=True, null=True)
    Week_End_End_Time = models.TimeField(blank=True, null=True)
    Week_Day_Start_Time = models.TimeField(blank=True, null=True)
    Week_Day_End_Time = models.TimeField(blank=True, null=True)
    Menu_File = models.FileField(upload_to='MenuFile/', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Menu'
