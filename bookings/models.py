from django.db import models
from users.models import User
from rooms.models import Room


class Booking(models.Model):
    """
    A model to create and manage bookings
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field=email)
    main_guest_name = models.CharField(max_length=200, blank=False)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, to_field=name)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
