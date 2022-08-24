import uuid

from django.db import models
from django.utils.crypto import get_random_string
from backend.settings import BOOKING_STATUS


# Create your models here.
class TableBooking(models.Model):
    BookingID = models.CharField(max_length=16, unique=True, null=True, blank=True)
    Booking_Time = models.TimeField()
    Booking_Date = models.DateField()
    Party_Size = models.IntegerField()
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telephone_Number = models.CharField(max_length=100)
    Type_of_Booking = models.BooleanField(default=False, null=True, blank=True, )
    Get_Emails = models.BooleanField(default=False, null=True, blank=True, )
    Status_booking = models.CharField(max_length=100, null=True, blank=True, choices=BOOKING_STATUS,
                                      default='Confirmed')

    def save(self, *args, **kwargs):
        if self.BookingID == "":
            self.BookingID = uuid.uuid4().hex.upper()[0:16]
        if self.BookingID is None:
            self.BookingID = uuid.uuid4().hex.upper()[0:16]
        super(TableBooking, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.id, self.BookingID)

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Bookings'


class BookTableCover(models.Model):
    cover_Img = models.ImageField(upload_to='BookingTable/')
    Caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.id, self.Caption)

    class Meta:
        verbose_name_plural = 'Book Table Cover'


class BookTableCover2(models.Model):
    cover_Img = models.ImageField(upload_to='BookingTable/', help_text='recommended dimensions 1000x403')
    Text = models.TextField()

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name_plural = 'Book Table Cover 2'
