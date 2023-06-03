from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'main_guest_name',
        'room',
        'check_in',
        'check_out',
    )
    list_filter = ('check_in',)
    search_fields = ('owner', 'main_guest_name', 'room',)
