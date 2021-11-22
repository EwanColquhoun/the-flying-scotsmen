from datetime import date
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


INSTRUCTOR_REQUIRED = (('No', 'No'), ('Yes', 'Yes'))
APPROVED = ((0, 'No'), (1, 'Yes'))
REPLIED = ((0, 'No'), (1, 'Yes'))


class Slot(models.Model):

    class Meta:
        ordering = ['start']

    slot = models.CharField(max_length=11, unique=True)
    start = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    admin = models.BooleanField(default=False)

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
    
    username = models.CharField(max_length=20)
    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        related_name='booked_aircraft'
    )
    date = models.DateField(default=date.today)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=False, blank=False)
    instructor_requested = models.CharField(max_length=5, choices=INSTRUCTOR_REQUIRED, default=False)
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
        
        if str(self.aircraft) == 'G-BSAI':
            if self.approved == 1:
                return f'<span class="btn-events aircraft-purple calendar-events" data-ref={self.approved} name={self.date.month}_{self.date.day}>{self.slot} | {self.username} | <i class="fas fa-check"></i> </span>'
            else:
                return f'<span class="btn-events calendar-events purple-transparent" data-ref={self.approved} name={self.date.month}_{self.date.day}>{self.slot} | {self.username} | <i class="fas fa-user-cog"></i></span>'
        elif self.approved == 1:
            return f'<span class="btn-events aircraft-green calendar-events" data-ref={self.approved} name={self.date.month}_{self.date.day}>{self.slot} | {self.username} | <i class="fas fa-check"></i></span>'
        else:
            return f'<span class="btn-events calendar-events green-transparent" data-ref={self.approved} name={self.date.month}_{self.date.day}>{self.slot} | {self.username} | <i class="fas fa-user-cog"></i></span>'


class Contact(models.Model):

    name = models.CharField(max_length=30, null=False, blank=False)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+441234567890'. Up to 15 digits allowed.")
    telephone = PhoneNumberField(null=False, blank=False,)
    email = models.EmailField(max_length=40, blank=False)
    message = models.TextField(blank=False)
    replied = models.IntegerField(choices=REPLIED, default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
