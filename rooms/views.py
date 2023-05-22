from django.views.generic import CreateView, ListView
from .models import Room
from .forms import AddRoomForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Rooms(ListView):
    """View for showing all rooms"""
    template_name = 'rooms/rooms.html'
    model = Room
    context_object_name = 'rooms'




class AddRoom(LoginRequiredMixin, CreateView):
    """
    View for creating rooms by staff
    """
    template_name = 'rooms/add_room.html'
    model = Room
    form_class = AddRoomForm
    success_url = '/rooms/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRoom, self).form_valid(form)

    
