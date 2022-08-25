from rest_framework import serializers
from .models import *


class TableBookingCheckSerializers(serializers.ModelSerializer):
    class Meta:
        model = TableBooking
        fields = ('Booking_Time', 'Booking_Date', 'Party_Size','Status_booking')


class TableBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = TableBooking
        fields = '__all__'


class BookTableCoverSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookTableCover
        fields = '__all__'

        def get_cover_Img(self, BookTableCover):
            try:
                request = self.context.get('request')
                if BookTableCover.PaperFile:
                    cover_Img = BookTableCover.cover_Img.url
                    return request.build_absolute_uri(cover_Img)
            except NameError:
                print(NameError)


class BookTableCover2Serializers(serializers.ModelSerializer):
    class Meta:
        model = BookTableCover2
        fields = '__all__'
