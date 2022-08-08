from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.
class TableBooking(models.Model):
    BookingID = models.CharField(max_length=12, null=True, blank=True)
    Booking_Time = models.TimeField()
    Booking_Date = models.DateField()
    Party_Size = models.IntegerField()
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Telephone_Number = models.CharField(max_length=100, null=True, blank=True)
    Type_of_Booking = models.BooleanField()
    Get_Emails = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.BookingID is None:
            self.BookingID = get_random_string(length=12)
        super(TableBooking, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.id, self.BookingID)

    class Meta:
        verbose_name_plural = 'Bookings'


class BookTableCover(models.Model):
    cover_Img = models.ImageField(upload_to='BookingTable/')
    Caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.id, self.Caption)

    class Meta:
        verbose_name_plural = 'Book Table Cover'


class BookTableCover2(models.Model):
    cover_Img = models.ImageField(upload_to='BookingTable/')

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Book Table Cover 2'
