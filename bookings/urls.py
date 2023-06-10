from django.urls import path
from .views import MakeBooking, BookingsList

urlpatterns = [
    path('newbooking/', MakeBooking.as_view(), name='new_booking'),
    path('', BookingsList.as_view(), name='mybookings'),
]