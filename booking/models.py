import datetime
from django.urls import reverse
from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from cloudinary.models import CloudinaryField

INSTRUCTOR_REQUIRED = ((0, 'No'), (1, 'Yes'))
APPROVED = ((0, 'No'), (1, 'Yes'))


class Slot(models.Model):

    class Meta:
        ordering = ['start']

    slot = models.CharField(max_length=11)
    start = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.slot)


class Aircraft(models.Model):
    reg = models.CharField(max_length=6, null=False, blank=False)
    desc = models.CharField(max_length=25, null=False, blank=False)
    aircraft_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.reg)


class Booking(models.Model):
    """
    Takes a booking registering the user, slot and aircraft.
    """
    
    username = models.CharField(max_length=30)
    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        related_name='booked_aircraft'
    )
    date = models.DateField()
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=False, blank=False)
    instructor_requested = models.IntegerField(choices=INSTRUCTOR_REQUIRED, default=False)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    approved = models.IntegerField(choices=APPROVED, default=False)

    class Meta:
        ordering = ['date', 'slot']

    def __str__(self):
        return str(self.aircraft)

    @property
    def get_html_url(self):
        url = reverse('edit_booking', args=(self.pk,))
        
        if str(self.aircraft) == 'G-BTXG':
            return f'<a class="btn-events aircraft-purple mt-2 calendar-events" name={self.date.day} href={url}>{self.slot} | {self.username}</a>'
        else:
            return f'<a class="btn-events aircraft-green mt-2 calendar-events" name={self.date.day} href={url}>{self.slot} | {self.username}</a>'