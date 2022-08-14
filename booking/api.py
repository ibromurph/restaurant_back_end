from django.core.mail import EmailMultiAlternatives, send_mail
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
            htmly = get_template('Email.html')
            data = {'firstname': "firstname", 'lastname': "lastname", 'activate_url': "activate_url"}
            subject, from_email, to = 'Welcome Dear' + " " + "firstname.capitalize()" + " " + "lastname.capitalize()" + "" + "Please Activate your account",'AltETWeb@outlook.com', 'abdullahrafi.ar@gmail.com'
            html_content = htmly.render(data)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TableBookingData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return TableBooking.objects.filter(id=self.kwargs['pk'])

    serializer_class = TableBookingSerializers


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
