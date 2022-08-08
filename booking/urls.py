from django.urls import path
from .api import *

urlpatterns = [
    path('TableBookingAPI/', TableBookingAPI.as_view(), name='TableBookingAPI Create'),
    path('TableBookingAPI/<int:pk>/', TableBookingData.as_view(), name='TableBookingAPI  RUD'),

    path('BookTableCoverAPI/', BookTableCoverAPI.as_view(), name='BookTableCoverAPI Create'),
    path('BookTableCoverAPI/<int:pk>/', BookTableCoverData.as_view(), name='BookTableCoverAPI  RUD'),

    path('BookTable2CoverAPI/', BookTable2CoverAPI.as_view(), name='BookTable2CoverAPI Create'),
    path('BookTable2CoverAPI/<int:pk>/', BookTable2CoverData.as_view(), name='BookTable2CoverAPI  RUD'),
]
