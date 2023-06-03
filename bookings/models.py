from django.db import models
from users.models import User
from rooms.models import Room

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
        User, on_delete=models.CASCADE, to_field=email)
    main_guest_name = models.CharField(
        max_length=200, default=User.get_full_name)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, to_field=name)
    check_in = models.DateField()
    check_out = models.DateField()
    no_of_ppl = models.IntegerField(choices=CAPACITY, default=1)
    breakfast = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_booking_length = 

    class Meta:
        ordering = ['check_in']
    
    def __str__(self):
        return str(self.pk)


