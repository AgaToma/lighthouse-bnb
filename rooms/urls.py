from django.urls import path
from .views import AddRoom, Rooms


urlpatterns = [
    path('add/', AddRoom.as_view(), name='add_room'),
    path('', Rooms.as_view(), name='rooms')
]