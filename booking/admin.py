from django.contrib import admin
from .models import *


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('BookingID', 'Booking_Time', 'Party_Size')
    fieldsets = (
        ('Info', {'fields': (
            'BookingID', 'Party_Size', 'First_Name', 'Last_Name', 'Email',
            'Telephone_Number', 'Type_of_Booking', 'Get_Emails')}),
        ("Booking Details", {"fields": (tuple(['Booking_Time', 'Booking_Date']),), }),
    )


admin.site.register(BookTableCover)
admin.site.register(BookTableCover2)
admin.site.register(TableBooking, BookingAdmin)
