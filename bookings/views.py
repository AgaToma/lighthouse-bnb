from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rooms.models import Room
from .models import Booking
from .forms import 


class MakeBooking(LoginRequiredMixin, CreateView):
    """
    View for logged in user to make their booking
    """
    form_class = BookingForm
    template_name = 'bookings/new_booking.html'
    success_url = '/rooms/'
    model = Booking

    def form_valid(self, form):
        form.instance.user = self.request.user
