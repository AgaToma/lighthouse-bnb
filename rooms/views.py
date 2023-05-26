from django.views.generic import CreateView, ListView, DetailView
from .models import Room
from .forms import AddRoomForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Rooms(ListView):
    """View for showing all rooms"""
    template_name = 'rooms/rooms.html'
    model = Room
    context_object_name = 'rooms'


class RoomDetails(DetailView):
    """View for showing room details"""
    template_name = 'rooms/room_details.html'
    model = Room
    context_object_name = 'room'


class AddRoom(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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

    def test_func(self):
        return self.request.user.is_admin

    
