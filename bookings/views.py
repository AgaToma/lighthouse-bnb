from django.views.generic import (CreateView, ListView,
                                  DetailView, DeleteView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from datetime import date, timedelta
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from users.models import CustomUser
from rooms.models import Room
from .models import Booking
from .forms import BookingForm, BookingEditForm


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

        messages.success(
            self.request,
            f'You have successfully booked {room}. Thank you for your booking')  
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
                return Booking.objects.filter(id=query)
            else:
                bookings = self.model.objects.filter(
                    check_in__gte=date.today() - timedelta(days=15))
                return bookings
        else:
            bookings = self.model.objects.filter(
                created_by=self.request.user.email,
                check_in__gte=date.today() - timedelta(days=15))
            return bookings
    

class BookingDetails(DetailView):
    """View for showing booking details"""
    template_name = 'bookings/booking_details.html'
    model = Booking
    context_object_name = 'booking_details'


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for editing own bookings for guests or all bookings for admins 
    """
    form_class = BookingEditForm
    template_name = 'bookings/edit_booking.html'
    success_url = '/bookings/'
    model = Booking
    
    def form_valid(self, form):
        
        room = form.cleaned_data['room']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']
        current_booking = form.instance
        
        # check room availability
        booking_list = Booking.objects.filter(room=room)
        new_booking_list = booking_list.exclude(id=current_booking.id)
        for booking in new_booking_list:
            if booking.check_in > check_out or booking.check_out < check_in:
                form.instance.room = room

        messages.success(
            self.request,
            'Your booking was successfully changed.')  
        return super(EditBooking, self).form_valid(form)
    
    def test_func(self):
        if self.request.user.is_admin:
            return True
        else:
            return self.request.user.email


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting bookings
    """
    model = Booking
    success_url = '/bookings/'
    template_name = 'bookings/delete_booking.html'

    def form_valid(self, form):
        messages.success(
            self.request,
            'Your booking was successfully deleted.'
        )
        return super(DeleteBooking, self).form_valid(form)
    
    def test_func(self):
        if self.request.user.is_admin:
            return True
        else:
            return self.request.user.email
            

        
        

