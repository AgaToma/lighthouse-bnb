from django.urls import path
from .views import MakeBooking, BookingsList, BookingDetails, EditBooking

urlpatterns = [
    path('newbooking/', MakeBooking.as_view(), name='new_booking'),
    path('', BookingsList.as_view(), name='mybookings'),
    path("<slug:pk>/", BookingDetails.as_view(), name='booking_details'),
    path("edit/<slug:pk>/", EditBooking.as_view(), name='edit_booking'),
]