from django.urls import path
from .api import *

urlpatterns = [
    path('MenuAPI/', MenuAPI.as_view(), name='MenuAPI Create'),
    path('MenuAPI/<int:pk>/', MenuData.as_view(), name='MenuAPI  RUD'),

    path('MenuCarouselAPI/', MenuCarouselAPI.as_view(), name='MenuCarouselAPI Create'),
    path('MenuCarouselAPI/<int:pk>/', MenuCarouselData.as_view(), name='MenuCarouselAPI  RUD'),
]
