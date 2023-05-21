from django.views.generic import CreateView
from .models import Room
from .forms import AddRoomForm


class AddRoom(CreateView):
    """
    View for creating rooms by staff
    """
    template_name = 'rooms/add_room.html'
    model = Room
    form_class = AddRoomForm
    success_url = '/rooms/'

    
