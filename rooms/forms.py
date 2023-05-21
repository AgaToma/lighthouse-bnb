from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Room


class AddRoomForm(forms.ModelForm):
    """
    Form to create a Room
    """
    class Meta:
        model = Room
        fields = ['name', 'room_no', 'view_type', 'capacity', 'description',
                  'image', 'image_alt']

        description = forms.CharField(widget=RichTextWidget())

        labels = {
            'name': 'Room Name',
            'room_no': 'Room Number',
            'view_type': 'View',
            'capacity': 'Maximum Number of People',
            'description': 'Description',
            'image': 'Room Image',
            'image_alt': 'Describe Image'
        }