from django.urls import path
from .views import AddRoom, Rooms


urlpatterns = [
    path('', AddRoom.as_view(), name='add_room'),
    path('rooms/', Rooms.as_view(), name='rooms')
]