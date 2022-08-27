from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import *



class MenuAPI(APIView):
    serializer_class = MenuSerializers

    def get(self, request):
        data = Menu.objects.all()
        serializer = MenuSerializers(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Menu.objects.filter(id=self.kwargs['pk'])

    serializer_class = MenuSerializers


class MenuCarouselAPI(APIView):
    serializer_class = MenuCarouselSerializers

    def get(self, request):
        data = MenuCarousel.objects.all()
        serializer = MenuCarouselSerializers(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuCarouselSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuCarouselData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return MenuCarousel.objects.filter(id=self.kwargs['pk'])

    serializer_class = MenuCarouselSerializers
