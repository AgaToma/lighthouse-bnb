from django.db import models
from datetime import date
from django.conf import settings
from rooms.models import Room
from users.models import CustomUser


# Choice fields
no_of_ppl = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
)


class Booking(models.Model):
    """
    A model to create and manage bookings
    """
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='email',
        blank=True)
    main_guest_name = models.CharField(
        max_length=200, default=CustomUser().get_full_name())
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, to_field='name')
    check_in = models.DateField()
    check_out = models.DateField()
    no_of_ppl = models.IntegerField(choices=no_of_ppl, default=1)
    breakfast = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['check_in']
      
    def __str__(self):
        return str(self.pk)

    @property
    def days_until(self):
        days_till = self.check_in - date.today()
        return days_till

    @property
    def booking_length(self):
        length = (self.check_out - self.check_in).days
        return length

    @property
    def get_price(self):
        booking_price = self.room.price * self.booking_length
        return booking_price

    @property
    def is_past_due(self):
        return date.today() > self.check_in


    


