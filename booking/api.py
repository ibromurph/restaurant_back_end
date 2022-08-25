from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import *
from django.template.loader import get_template

from backend.settings import AvailableSlots


class TableBookingAvailability(APIView):
    serializer_class = TableBookingCheckSerializers

    def post(self, request, format=None):
        Final_Slots = []
        Booking_Date_d = request.data.get('Booking_Date')
        Booking_Time_d = request.data.get('Booking_Time')
        Party_Size_d = request.data.get('Party_Size')
        Total_Party_size = 60
        Index_Date = []

        for (x, y) in AvailableSlots:
            if x == Booking_Time_d:
                Index_Date = AvailableSlots.index((x, y))

        for x in range(Index_Date, len(AvailableSlots)):
            table_rows = TableBooking.objects.filter(Booking_Date=Booking_Date_d).filter(
                Booking_Time=AvailableSlots[x][0])
            Total_count = 0
            for row in table_rows:
                Total_count += row.Party_Size
            if int(Total_count) + int(Party_Size_d) <= Total_Party_size:
                Final_Slots.append(AvailableSlots[x][0])

        if len(Final_Slots) >= 0:
            return Response({"Slots": Final_Slots[0:16]})
        else:
            raise Http404


class TableBookingAPI(APIView):
    serializer_class = TableBookingSerializers

    def get(self, request):
        data = TableBooking.objects.all()
        serializer = TableBookingSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TableBookingSerializers(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            data_s = serializer.data
            id = data_s['id']
            TableData = TableBooking.objects.get(id=id)
            htmly = get_template('Email.html')
            firstname = TableData.First_Name
            lastname = TableData.Last_Name
            Email = TableData.Email
            BookingID = TableData.BookingID
            Status_booking = TableData.Status_booking
            Booking_Time = TableData.Booking_Time
            Booking_Date = TableData.Booking_Date
            Party_Size = TableData.Party_Size

            # data = {'firstname': firstname, 'lastname': lastname, "Status_booking": Status_booking,
            #         "Booking_Time": Booking_Time, "Booking_Date": Booking_Date, "Party_Size": Party_Size,
            #         "BookingID": BookingID}
            # subject, from_email, to = 'Greetings' + " " + firstname.capitalize() + " " + lastname.capitalize() + "" + "Confirmation of your booking", 'Altetweb@outlook.com', Email
            # html_content = htmly.render(data)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableBookingData(APIView):
    def get_object(self, pk):
        try:
            return TableBooking.objects.get(pk=pk)
        except TableBooking.DoesNotExist:
            raise Http404

    def get_object_all(self):
        try:
            TableBooking.objects.all()
        except TableBooking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TableBookingSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        data = request.data

        try:
            TableBooking.objects.filter(pk=pk)
            successMessage = 'Rating Updated'
            return Response({"message": successMessage}, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({"message": ex}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def Sendemail(data):
    bookingid = data.get().BookingID
    firstname = data.get().First_Name
    lastname = data.get().Last_Name
    Email = data.get().Email
    Booking_Time = data.get().Booking_Time
    Booking_Date = data.get().Booking_Date

    htmly = get_template('Cancelled.html')
    data = {'firstname': firstname, 'lastname': lastname, "Status_booking": "Cancelled",
            "Booking_Time": Booking_Time, "Booking_Date": Booking_Date,
            "BookingID": bookingid}
    subject, from_email, to = 'Greetings' + " " + firstname.capitalize() + " " + lastname.capitalize() + "" + " Cancellation of your booking", 'Altetweb@outlook.com', Email
    html_content = htmly.render(data)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


class CancelTableBookingVIABID(APIView):
    def put(self, request, *args, **kwargs):
        bookingID = self.kwargs['bookingID']
        try:
            data = TableBooking.objects.filter(BookingID=bookingID)
            if len(data):
                data.update(Status_booking='Cancelled')
                # Sendemail(data)
                return Response({"message": 'Your Booking is Cancelled'})
            else:
                return Response({"message": 'No booking Found'})
        except Exception as ex:
            return Response({"message": ex})


class CancelTableBookingVIAEmail(APIView):
    def get(self, request, *args, **kwargs):
        Email = self.kwargs['email']
        data = TableBooking.objects.filter(Email=Email)
        serializer = TableBookingSerializers(data, many=True)

        if len(serializer.data) > 0:
            return Response(serializer.data)
        else:
            raise Http404
            # print(serializer.errors)
            # return Response({"serializer.errors, status=status.HTTP_400_BAD_REQUEST"})


class BookTableCoverAPI(APIView):
    serializer_class = BookTableCoverSerializers

    def get(self, request):
        data = BookTableCover.objects.all()
        serializer = BookTableCoverSerializers(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookTableCoverSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookTableCoverData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return BookTableCover.objects.filter(id=self.kwargs['pk'])

    serializer_class = BookTableCoverSerializers


class BookTable2CoverAPI(APIView):
    serializer_class = BookTableCover2Serializers

    def get(self, request):
        data = BookTableCover2.objects.all()
        serializer = BookTableCover2Serializers(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookTableCover2Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookTable2CoverData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return BookTableCover2.objects.filter(id=self.kwargs['pk'])

    serializer_class = BookTableCover2Serializers
