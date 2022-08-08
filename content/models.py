from django.db import models
from backend.settings import CHOICES
from colorfield.fields import ColorField


class SocialMedia(models.Model):
    Facebook = models.CharField(max_length=100, null=True, blank=True)
    Instagram = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Social Media'


class Carousel(models.Model):
    Image = models.ImageField(upload_to='Carousel/', null=True, blank=True)
    ImageOpacity = models.IntegerField(null=True, blank=True, help_text='Enter in Percentage')
    Caption_Heading = models.CharField(max_length=100, null=True, blank=True)
    Color_Caption_Heading = ColorField(default='#FF0000')
    Caption_subHeading = models.CharField(max_length=100, null=True, blank=True)
    Color_Caption_subHeading = ColorField(default='#FF0000')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Carousel'


class Timing(models.Model):
    Weekdays_Start_Time = models.TimeField(null=True, blank=True)
    Weekdays_End_Time = models.TimeField(null=True, blank=True)

    WeekEndTime_Start_Time = models.TimeField(null=True, blank=True)
    WeekEndTime_End_Time = models.TimeField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     id_exist = Timing.objects.exists()
    #     if id_exist:
    #         id = Timing.objects.all().last()
    #         print(self.Weekdays_Start_Time)
    #         Weekdays_Start_Time = self.Weekdays_Start_Time
    #
    #         # id.objects.filter(id=id).update(Weekdays_Start_Time=Weekdays_Start_Time),
    #         #                                 Weekdays_End_Time=self.Weekdays_End_Time,
    #         #                                 WeekEndTime_Start_Time=self.WeekEndTime_Start_Time,
    #         #                                 WeekEndTime_End_Time=self.WeekEndTime_End_Time)
    #         print("empty")
    #     super(Timing, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Timing'


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
    Days = models.ManyToManyField(to=MenuDay)
    Menu_File = models.FileField(upload_to='MenuFile/', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Menu'


class InstagramPost(models.Model):
    Post_Image = models.ImageField(upload_to='Instagram', null=True, blank=True,
                                   help_text='Recommended Dimensions 500x500')
    URL = models.URLField(null=True, blank=True, help_text='Paste IG Link e.g https://www.instagram.com/')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Instagram Post'


class ContactUs(models.Model):
    PhoneNumber = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    GoogleMaps = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Contact Us'


class BrandLogo(models.Model):
    Logo = models.ImageField(upload_to='BrandLogo/')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Brand Logo'


class AboutUs(models.Model):
    Paragraph = models.TextField()

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'About Us'


class HomePageImage(models.Model):
    Img = models.ImageField(upload_to='HomePageImg/')
    Heading1 = models.CharField(max_length=100, null=True, blank=True)
    Paragraph = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'HomePage Image'


class AddressDetails(models.Model):
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Address & Details'
