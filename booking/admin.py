from django.contrib import admin
from django import forms
from .models import Booking, Aircraft, Slot, Contact, Group_Member


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    """
    Manages Aircraft
    """
    list_filter = ('reg', 'desc',)
    list_display = ('reg', 'desc',)
    search_fields = ['reg', ]


@admin.register(Group_Member)
class Group_MemberAdmin(admin.ModelAdmin):

    list_filter = ('registered', 'date_joined',)
    list_display = ('user', 'registered', 'message', 'date_joined',)
    search_fields = ['user', 'registered', 'date_joined', ]

    def register_member(self, request, queryset):
        queryset.update(registered=True)
        

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    """
    Manages Slot allocation
    """
    class Meta:
        ordering = ['start']
        fields = ('start', 'duration', )
        widgets = {
            'start': forms.TimeInput(format='%H:%M'),
            'duration': forms.TimeInput(format='%H'),
        }
    list_filter = ('slot', 'start')
    list_display = ('slot', 'start')
    search_fields = ['slot', 'start']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Manages bookings
    """
    class Meta:
        model = Booking
        widgets = {
          'notes': forms.Textarea(attrs={'rows': 5, 'cols': 33,}),        
        }

    list_filter = ('date', 'aircraft', 'username', 'instructor_requested', 'approved')
    list_display = ('date', 'slot', 'aircraft', 'username', 'instructor_requested', 'created_on', 'notes', 'approved')
    search_fields = ['date', 'aircraft', 'username', 'instructor_requested']
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Manages contact requests
    """
    class Meta:
        model = Contact
        widgets = {
          'message': forms.Textarea(attrs={'rows': 5, 'cols': 33}),
          'telephone': forms.Textarea(attrs={'placeholder': 'Including country code'}),
        }

    actions = ['replied']
    list_filter = ('name', 'telephone', 'email', 'message', 'replied')
    list_display = ('name', 'telephone', 'email', 'message', 'replied')
    search_fields = ['name', 'telephone', 'email', 'message', 'replied']

    def replied(self, request, queryset):
        queryset.update(replied=True)
