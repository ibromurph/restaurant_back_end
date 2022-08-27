import uuid

from django.db import models
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField


class SocialMedia(models.Model):
    Facebook = models.CharField(max_length=100, null=True, blank=True)
    Instagram = models.CharField(max_length=100, null=True, blank=True)
    Twitter = models.CharField(max_length=100, null=True, blank=True)
    Pinterest = models.CharField(max_length=100, null=True, blank=True)
    Dribbble = models.CharField(max_length=100, null=True, blank=True)
    Behance = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            self.__class__.objects.get(id=self.id)
            return super(SocialMedia, self).save(*args, **kwargs)
        except Exception as e:
            if self.__class__.objects.all().count() >= 1:
                return None
            return super(SocialMedia, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        try:
            self.__class__.objects.get(id=self.id)
            return super(Timing, self).save(*args, **kwargs)
        except Exception as e:
            if self.__class__.objects.all().count() >= 1:
                return None
            return super(Timing, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Timing'


class InstagramPost(models.Model):
    Post_Image = models.ImageField(upload_to='Instagram', null=True, blank=True,
                                   help_text='Recommended Dimensions 500x500')
    URL = models.URLField(null=True, blank=True, help_text='Paste IG Link e.g https://www.instagram.com/')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Instagram Post'


class ContactUs(models.Model):
    Phone = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Google_Maps = models.CharField(max_length=200, null=True, blank=True,
                                   help_text='https://goo.gl/maps/F1f2KFSW4ByHsQveA')
    Email = models.EmailField()

    def save(self, *args, **kwargs):
        try:
            self.__class__.objects.get(id=self.id)
            return super(ContactUs, self).save(*args, **kwargs)
        except Exception as e:
            if self.__class__.objects.all().count() >= 1:
                return None
            return super(ContactUs, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Find Us'


class ContactUsPage(models.Model):
    Image = models.ImageField(upload_to='Contactus/')
    AboutUs = models.TextField()

    def save(self, *args, **kwargs):
        try:
            self.__class__.objects.get(id=self.id)
            return super(ContactUsPage, self).save(*args, **kwargs)
        except Exception as e:
            if self.__class__.objects.all().count() >= 1:
                return None
            return super(ContactUsPage, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Contact Us Page'


class ContactedUs(models.Model):
    TicketID = models.CharField(max_length=100, unique=True, null=True, blank=True)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Subject = models.CharField(max_length=200)
    Message = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.TicketID == "":
            self.TicketID = str(uuid.uuid4().hex[0:3]) + "-" + str(uuid.uuid4().hex.upper()[0:5])
        if self.TicketID is None:
            self.TicketID = str(uuid.uuid4().hex[0:3]) + "-" + str(uuid.uuid4().hex.upper()[0:5])
        super(ContactedUs, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.id, self.Name)

    class Meta:
        verbose_name_plural = 'Contacted Us'


class BrandLogo(models.Model):
    Logo = models.ImageField(upload_to='BrandLogo/')

    def save(self, *args, **kwargs):
        try:
            self.__class__.objects.get(id=self.id)
            return super(BrandLogo, self).save(*args, **kwargs)
        except Exception as e:
            if self.__class__.objects.all().count() >= 1:
                return None
            return super(BrandLogo, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Brand Logo'


class AboutUs(models.Model):
    CoverImage = models.ImageField(upload_to='AboutUs/', null=True, blank=True)
    Paragraph = models.TextField()
    Paragraph2 = RichTextField()

    def save(self, *args, **kwargs):
        try:
            self.__class__.objects.get(id=self.id)
            return super(AboutUs, self).save(*args, **kwargs)
        except Exception as e:
            if self.__class__.objects.all().count() >= 1:
                return None
            return super(AboutUs, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'About Us'


class HomePageImage(models.Model):
    Img = models.ImageField(upload_to='HomePageImg/')
    Heading1 = models.CharField(max_length=100, null=True, blank=True)
    Paragraph = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            self.__class__.objects.get(id=self.id)
            return super(HomePageImage, self).save(*args, **kwargs)
        except Exception as e:
            if self.__class__.objects.all().count() >= 1:
                return None
            return super(HomePageImage, self).save(*args, **kwargs)

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
