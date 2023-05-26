from django.urls import path
from .views import AddRoom, Rooms, RoomDetails, DeleteRoom


urlpatterns = [
    path('add/', AddRoom.as_view(), name='add_room'),
    path('', Rooms.as_view(), name='rooms'),
    path("<slug:pk>/", RoomDetails.as_view(), name='room_details'),
    path('delete/<slug:pk>/', DeleteRoom.as_view(), name='delete_room')
]