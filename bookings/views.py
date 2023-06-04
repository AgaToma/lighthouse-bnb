from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rooms.models import Room
from .models import Booking
from .forms import BookingForm


class MakeBooking(LoginRequiredMixin, CreateView):
    """
    View for logged in user to make their booking of selected room
    """
    form_class = BookingForm
    template_name = 'bookings/new_booking.html'
    success_url = '/rooms/'
    model = Booking

    def form_valid(self, form):
        form.instance.user = self.request.user
        room = form.cleaned_data['room']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']

        # get existing bookings for the room
        booking_list = Booking.objects.filter(room=room)
        # check if there already are bookings on specified dates
        for booking in booking_list:
            if booking.check_in > check_in and booking.check_out > 