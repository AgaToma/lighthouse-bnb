from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'room_no',
        'view_type',
        'capacity',
        'description',
        'image'
    )
    list_filter = ('capacity',)


admin.site.register(Room)