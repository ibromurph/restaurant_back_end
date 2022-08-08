from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import *


class SocialMediaAPI(APIView):
    serializer_class = SocialMediaSerializers

    def get(self, request):
        data = SocialMedia.objects.all()
        serializer = SocialMediaSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SocialMediaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialMediaData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return SocialMedia.objects.filter(id=self.kwargs['pk'])

    serializer_class = SocialMediaSerializers


class CarouselAPI(APIView):
    serializer_class = CarouselSerializers

    def get(self, request):
        data = Carousel.objects.all()
        serializer = CarouselSerializers(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarouselSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarouselData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Carousel.objects.filter(id=self.kwargs['pk'])

    serializer_class = CarouselSerializers


class TimingAPI(APIView):
    serializer_class = TimingSerializers

    def get(self, request):
        data = Timing.objects.all()
        serializer = TimingSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TimingSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimingData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Timing.objects.filter(id=self.kwargs['pk'])

    serializer_class = TimingSerializers


class MenuDayAPI(APIView):
    serializer_class = MenuDaySerializers

    def get(self, request):
        data = MenuDay.objects.all()
        serializer = MenuDaySerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuDaySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDayData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return MenuDay.objects.filter(id=self.kwargs['pk'])

    serializer_class = MenuDaySerializers


class MenuAPI(APIView):
    serializer_class = MenuSerializers

    def get(self, request):
        data = Menu.objects.all()
        serializer = MenuSerializers(data, many=True)
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


class InstagramPostAPI(APIView):
    serializer_class = InstagramPostSerializers

    def get(self, request):
        data = InstagramPost.objects.all()
        serializer = InstagramPostSerializers(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InstagramPostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstagramPostData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return InstagramPost.objects.filter(id=self.kwargs['pk'])

    serializer_class = InstagramPostSerializers


class ContactUsAPI(APIView):
    serializer_class = ContactUsSerializers

    def get(self, request):
        data = ContactUs.objects.all()
        serializer = ContactUsSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactUsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactUsData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return ContactUs.objects.filter(id=self.kwargs['pk'])

    serializer_class = ContactUsSerializers


class BrandLogoAPI(APIView):
    serializer_class = BrandLogoSerializers

    def get(self, request):
        data = BrandLogo.objects.all()
        serializer = BrandLogoSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BrandLogoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandLogoData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return BrandLogo.objects.filter(id=self.kwargs['pk'])

    serializer_class = BrandLogoSerializers


class AboutUsAPI(APIView):
    serializer_class = AboutUsSerializers

    def get(self, request):
        data = AboutUs.objects.all()
        serializer = AboutUsSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AboutUsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutUsData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return AboutUs.objects.filter(id=self.kwargs['pk'])

    serializer_class = AboutUsSerializers


class HomePageImageAPI(APIView):
    serializer_class = HomePageImageSerializers

    def get(self, request):
        data = HomePageImage.objects.all()
        serializer = HomePageImageSerializers(data, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HomePageImageSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomePageImageData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return HomePageImage.objects.filter(id=self.kwargs['pk'])

    serializer_class = HomePageImageSerializers


class AddressDetailsAPI(APIView):
    serializer_class = AddressDetailsSerializers

    def get(self, request):
        data = AddressDetails.objects.all()
        serializer = AddressDetailsSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetailsData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return AddressDetails.objects.filter(id=self.kwargs['pk'])

    serializer_class = AddressDetailsSerializers
