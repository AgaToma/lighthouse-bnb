from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'room_no',
        'view_type',
        'capacity',
        'description',
        'id'
    )
    list_filter = ('capacity',)
    search_fields = ('name', 'room_no', 'capacity', 'view_type')
