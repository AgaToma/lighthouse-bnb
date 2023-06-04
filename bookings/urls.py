from django.urls import path
from .views import MakeBooking

urlpatterns = [
    path('newbooking/', MakeBooking.as_view(), name='new_booking')
]