from datetime import date
from rooms.models import Room
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Form to create a new booking
    """
    class Meta:
        model = Booking
        fields = ['main_guest_name', 'check_in', 'check_out', 'no_of_ppl',
                  'breakfast']
        labels = {
            'main_guest_name': 'Main Guest Name',
            'check_in': 'Check In Date',
            'check_out': 'Check Out Date',
            'no_of_ppl': 'Number of Guests',
            'breakfast': 'Include Breakfast?'
        }
