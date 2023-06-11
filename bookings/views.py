from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date, timedelta
from django.contrib import messages
from django.db.models import Q
from users.models import CustomUser
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
        
        form.instance.created_by = self.request.user
        room = form.cleaned_data['room']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']
        
        # check room availability
        booking_list = Booking.objects.filter(room=room)
        for booking in booking_list:
            if booking.check_in > check_out or booking.check_out < check_in:
                form.instance.room = room
                # messages.success(
                    # self.request,
                    # f'Thank you for your booking. Your booking id is {self.id}')
                    
        return super(MakeBooking, self).form_valid(form)


class BookingsList(LoginRequiredMixin, ListView):
    """View for showing bookings for authenticated user"""
    template_name = 'bookings/mybookings.html'
    model = Booking
    context_object_name = 'bookings'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')

        if self.request.user.is_admin:
            if query:
                bookings = self.model.objects.filter(
                    Q(check_in__icontains=query) |
                    Q(created_by__icontains=query) |
                    Q(main_guest_name__icontains=query) |
                    Q(room__icontains=query))
            else:
                bookings = Booking.objects.all()
                return bookings
        else:
            bookings = self.model.objects.filter(
                created_by=self.request.user.email)
            return bookings


class BookingDetails(DetailView):
    """View for showing booking details"""
    template_name = 'bookings/booking_details.html'
    model = Booking
    context_object_name = 'booking_details'
    
            

        
        

