from django.urls import path
from .api import *

urlpatterns = [

    path('SocialMedia/', SocialMediaAPI.as_view(), name='SocialMedia Create'),
    path('SocialMedia/<int:pk>/', SocialMediaData.as_view(), name='SocialMedia RUD'),

    path('CarouselAPI/', CarouselAPI.as_view(), name='CarouselAPI Create'),
    path('CarouselAPI/<int:pk>/', CarouselData.as_view(), name='CarouselAPI RUD'),

    path('TimingAPI/', TimingAPI.as_view(), name='TimingAPI Create'),
    path('TimingAPI/<int:pk>/', TimingData.as_view(), name='TimingAPI  RUD'),


    path('InstagramPostAPI/', InstagramPostAPI.as_view(), name='InstagramPostAPI Create'),
    path('InstagramPostAPI/<int:pk>/', InstagramPostData.as_view(), name='InstagramPostAPI  RUD'),

    path('ContactUsAPI/', ContactUsAPI.as_view(), name='ContactUsAPI Create'),
    path('ContactUsAPI/<int:pk>/', ContactUsData.as_view(), name='ContactUsAPI  RUD'),

    path('ContactUsAPI/', ContactUsAPI.as_view(), name='ContactUsAPI Create'),
    path('ContactUsAPI/<int:pk>/', ContactUsData.as_view(), name='ContactUsAPI  RUD'),

    path('BrandLogoAPI/', BrandLogoAPI.as_view(), name='BrandLogoAPI Create'),
    path('BrandLogoAPI/<int:pk>/', BrandLogoData.as_view(), name='BrandLogoAPI  RUD'),

    path('AboutUsAPI/', AboutUsAPI.as_view(), name='AboutUsAPI Create'),
    path('AboutUsAPI/<int:pk>/', AboutUsData.as_view(), name='AboutUsAPI  RUD'),

    path('HomePageImageAPI/', HomePageImageAPI.as_view(), name='AboutUsAPI Create'),
    path('HomePageImageAPI/<int:pk>/', HomePageImageData.as_view(), name='AboutUsAPI  RUD'),

    path('AddressDetailsAPI/', AddressDetailsAPI.as_view(), name='AddressDetailsAPI Create'),
    path('AddressDetailsAPI/<int:pk>/', AddressDetailsData.as_view(), name='AddressDetailsAPI  RUD'),

]
