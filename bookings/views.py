from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date
from django.contrib import messages
from rooms.models import Room
from .models import Booking
from .forms import BookingForm


class MakeBooking(LoginRequiredMixin, CreateView):
    """
    View for logged in user to make their booking of selected room
    """
    form_class = BookingForm
    template_name = 'bookings/new_booking.html'
    success_url = '/bookings/'
    model = Booking

    def form_valid(self, form):
        form.instance.user = self.request.user
        room = form.cleaned_data['room']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']

        # check room availability
        booking_list = Booking.objects.filter(room=room)
        for booking in booking_list:
            if booking.check_in.date() > check_out.date() or
            booking.check_out.date() < check_in.date():
                form.instance.room = room
                messages.success(
                    self.request,
                    f'Thank you for your booking. Your booking id is {self.pk}')
        
    return super(MakeBooking, self).form_valid(form)
            

        
        

