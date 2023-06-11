from django.urls import path
from .views import MakeBooking, BookingsList, BookingDetails

urlpatterns = [
    path('newbooking/', MakeBooking.as_view(), name='new_booking'),
    path('', BookingsList.as_view(), name='mybookings'),
     path("<slug:pk>/", BookingDetails.as_view(), name='booking_details'),
]