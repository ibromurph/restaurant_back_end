from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import *
from django.template.loader import get_template


class TableBookingAPI(APIView):
    serializer_class = TableBookingSerializers

    def get(self, request):
        data = TableBooking.objects.all()
        serializer = TableBookingSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TableBookingSerializers(data=request.data)
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

            data = {'firstname': firstname, 'lastname': lastname, "Status_booking": Status_booking,
                    "Booking_Time": Booking_Time, "Booking_Date": Booking_Date, "Party_Size": Party_Size,
                    "BookingID": BookingID}
            subject, from_email, to = 'Greetings' + " " + firstname.capitalize() + " " + lastname.capitalize() + "" + "Confirmation of your booking", 'Altetweb@outlook.com', "abdullahrafi.ar@gmail.com "
            html_content = htmly.render(data)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
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


# class TableBookingData(generics.RetrieveUpdateDestroyAPIView):
#     def get_queryset(self):
#         return TableBooking.objects.filter(id=self.kwargs['pk'])
#
#     serializer_class = TableBookingSerializers


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
