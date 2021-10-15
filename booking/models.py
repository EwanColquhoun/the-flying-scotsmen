from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


INSTRUCTOR_REQUIRED = ((0, 'No'), (1, 'Yes'))
SLOT = (('0800-1000', '0800-1000'), ('1000-1200', '1000-1200'), 
        ('1200-1400', '1200-1400'), ('1400-1600', '1400-1600'), ('1600-1800', '1600-1800'))


class Aircraft(models.Model):
    reg = models.CharField(max_length=6, null=False, blank=False)
    desc = models.CharField(max_length=25, null=False, blank=False)
    aircraft_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.reg


class Slot(models.Model):
    time = models.CharField(max_length=11, choices=SLOT)

    def __str__(self):
        return self.time


class Booking(models.Model):
    """
    Takes a booking registering the user, slot and aircraft.
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_creator')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='booked_aircraft')
    date = models.DateField()
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='booked_slot')
    instructor_requested = models.IntegerField(choices=INSTRUCTOR_REQUIRED)
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'Booking on {self.date} at {self.slot} by {self.username}'

