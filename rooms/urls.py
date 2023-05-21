from django.urls import path
from .views import AddRoom


urlpatterns = [
    path('', AddRoom.as_view(), name='add_room')
]