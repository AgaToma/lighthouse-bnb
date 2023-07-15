from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from .models import Room
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Rooms(ListView):
    """View for showing all rooms"""
    template_name = 'rooms/rooms.html'
    model = Room
    context_object_name = 'rooms'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            rooms = self.model.objects.filter(
                Q(name__icontains=query) |
                Q(capacity__icontains=query) |
                Q(view_type__icontains=query)
            )
        else:
            rooms = self.model.objects.all()
        return rooms


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
    form_class = RoomForm
    success_url = '/rooms/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRoom, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_admin


class EditRoom(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating rooms by staff
    """
    template_name = 'rooms/edit_room.html'
    model = Room
    success_url = '/rooms/'
    form_class = RoomForm

    def test_func(self):
        return self.request.user.is_admin


class DeleteRoom(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting rooms by staff
    """
    model = Room
    success_url = '/rooms/'
    template_name = 'rooms/delete_room.html'

    def test_func(self):
        return self.request.user.is_admin
