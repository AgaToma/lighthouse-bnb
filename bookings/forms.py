from datetime import date
from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rooms.models import Room
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form to create a new booking
    """
    class Meta:
        model = Booking
        room = forms.ModelChoiceField(
            queryset=Room.objects.filter(), to_field_name='name')
        fields = ['room', 'main_guest_name', 'check_in', 'check_out',
                  'no_of_ppl', 'breakfast']
        labels = {
            'main_guest_name': 'Main Guest Name',
            'check_in': 'Check In Date',
            'check_out': 'Check Out Date',
            'no_of_ppl': 'Number of Guests',
            'breakfast': 'Include Breakfast?'
        }

    check_in = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))

    check_out = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))

    def clean(self):
        room = self.cleaned_data['room']
        check_in = self.cleaned_data['check_in']
        check_out = self.cleaned_data['check_out']
        no_of_ppl = self.cleaned_data['no_of_ppl']

        # check if selected room has correct capacity
        if room not in Room.objects.filter(capacity__gte=no_of_ppl):
            raise ValidationError(_(
                        'Your selected room is too small for' +
                        '%s people. Please choose a bigger room') % no_of_ppl)

        # validate check in date is before checkout
        if check_in > check_out or check_in == check_out:
            raise ValidationError(
                        'Check_in date needs to be before check_out date')

        # get all room bookings and check for availability
        bookings_list = Booking.objects.filter(room=room)
        availability = []
        for booking in bookings_list:
            if booking.check_in >= check_out or booking.check_out <= check_in:
                availability.append(True)
            else:
                availability.append(False)
        if all(availability) is False:
            raise ValidationError(
                        'This room is not available on the selected dates')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].empty_label = None


class BookingEditForm(forms.ModelForm):
    """
    Form to edit an existing booking
    """
    class Meta:
        model = Booking
        room = forms.ModelChoiceField(
            queryset=Room.objects.filter(), to_field_name='name')
        fields = ['room', 'main_guest_name', 'check_in', 'check_out',
                  'no_of_ppl', 'breakfast']
        labels = {
            'main_guest_name': 'Main Guest Name',
            'check_in': 'Check In Date',
            'check_out': 'Check Out Date',
            'no_of_ppl': 'Number of Guests',
            'breakfast': 'Include Breakfast?'
        }

    check_in = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))

    check_out = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))

    def clean(self):
        room = self.cleaned_data['room']
        check_in = self.cleaned_data['check_in']
        check_out = self.cleaned_data['check_out']
        no_of_ppl = self.cleaned_data['no_of_ppl']

        # check if there is booking made that will be edited now
        current_booking = None
        try:
            current_booking = Booking.objects.get(id=self.instance.pk)
        except ObjectDoesNotExist:
            pass

        # check if selected room has correct capacity
        if room not in Room.objects.filter(capacity__gte=no_of_ppl):
            raise ValidationError(_(
                        'Your selected room is too small for ' +
                        '%s people. Please choose a bigger room') % no_of_ppl)

        # validate check in date is before checkout
        if check_in > check_out or check_in == check_out:
            raise ValidationError(
                        'Check_in date needs to be before check_out date')

        # get all room bookings and check for availability
        bookings_list = Booking.objects.filter(room=room)
        new_bookings_list = bookings_list.exclude(id=current_booking.id)
        availability = []
        for booking in new_bookings_list:
            if booking.check_in >= check_out or booking.check_out <= check_in:
                availability.append(True)
            else:
                availability.append(False)
        if all(availability) is False:
            raise ValidationError(
                        'This room is not available on the selected dates')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].empty_label = None
