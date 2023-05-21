from django.views.generic import CreateView
from .models import Room
from .forms import AddRoomForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
        return super(AddRoom, seld).form_valid(form)

    
