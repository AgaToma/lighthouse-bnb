from django.db import models
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Choice Fields
VIEW_TYPES = (
    ('ocean', 'Ocean'),
    ('mountain', 'Mountain'),
    ('garden', 'Garden')
)

CAPACITY = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
)


class Room(models.Model):
    """
    A model to create and manage rooms
    """
    name = models.CharField(max_length=150, null=False, blank=False)
    room_no = models.IntegerField(null=False, blank=False)
    view_type = models.CharField(max_length=50, choices=VIEW_TYPES, default='ocean')
    capacity = models.IntegerField(choices=CAPACITY, default=1)
    description = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="rooms/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
   
    class Meta:
        ordering = ['-capacity']

    def __str__(self):
        return str(self.name)
