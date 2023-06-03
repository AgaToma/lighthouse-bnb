from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'created_by',
        'main_guest_name',
        'room',
        'check_in',
        'check_out',
        'id'
    )
    list_filter = ('check_in',)
    search_fields = ('id', 'created_by', 'main_guest_name', 'room',)
