from datetime import date
from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        check_in = self.cleaned_data['check_in']
        check_out = self.cleaned_data['check_out']
        no_of_ppl = self.cleaned_data['no_of_ppl']

        # check if selected room has correct capacity

        # get all room bookings and check for availability

        # if no availability redirect to general booking
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['check_in'].widget.attrs['class'] = 'datepicker'
        self.fields['check_out'].widget.attrs['class'] = 'datepicker'
        self.fields['room'].empty_label = None


