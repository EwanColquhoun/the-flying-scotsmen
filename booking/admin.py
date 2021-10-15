from django.contrib import admin
from .models import Booking, Aircraft, Slot


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    """
    Manages Aircraft
    """
    list_filter = ('reg', 'desc',)
    list_display = ('reg', 'desc',)
    search_fields = ['reg',]


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    """
    Manages Slot allocation
    """
    list_filter = ('time',)
    list_display = ('time',)
    search_fields = ['time']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Manages bookings
    """
    list_filter = ('date', 'aircraft', 'username', 'instructor_requested')
    list_display = ('date', 'slot', 'aircraft', 'username', 'instructor_requested', 'created_on')
    search_fields = ['date', 'aircraft', 'username', 'instructor_requested']
    actions = ['approve_bookings']