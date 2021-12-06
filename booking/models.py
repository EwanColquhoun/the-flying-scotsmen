from datetime import date
from django.urls import reverse
from django.db import models
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField


INSTRUCTOR_REQUIRED = (('No', 'No'), ('Yes', 'Yes'))
APPROVED = ((0, 'No'), (1, 'Yes'))
REPLIED = ((0, 'No'), (1, 'Yes'))


class Slot(models.Model):
    """
    Allows Admin to alter the slots.
    """

    class Meta:
        ordering = ['start']

    slot = models.CharField(max_length=11, unique=True)
    start = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.slot)


class Aircraft(models.Model):
    """
    Lets Admin register the Aircraft details.
    """
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
    slot = models.ForeignKey(
        Slot,
        on_delete=models.CASCADE,
        null=False,
        blank=False)
    instructor_requested = models.CharField(
        max_length=5,
        choices=INSTRUCTOR_REQUIRED,
        default=False)
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
        """
        Displays the booking as a span in the Calendar
        """
        url = reverse('edit_booking', args=(self.pk,))

        if str(self.aircraft) == 'G-BSAI':
            if self.approved == 1:
                return (
                    f'<span class="btn-events aircraft-purple calendar-events"'
                    f'data-ref={self.approved} name={self.date.month}_'
                    f'{self.date.day}>{self.slot}'
                    f' | {self.username} | <i class="fas fa-check"></i></span>'
                )
            else:
                return (
                    f'<span class="btn-events calendar-events purple-trans"'
                    f' data-ref={self.approved} name={self.date.month}_'
                    f'{self.date.day}>{self.slot} | {self.username} | '
                    f'<i class="fas fa-user-cog"></i></span>'
                )
        elif self.approved == 1:
            return (
                f'<span class="btn-events aircraft-green calendar-events"'
                f'data-ref={self.approved} name={self.date.month}_'
                f'{self.date.day}>{self.slot} | {self.username}'
                f' | <i class="fas fa-check"></i></span>'
            )
        else:
            return (
                f'<span class="btn-events calendar-events green-trans"'
                f' data-ref={self.approved} name={self.date.month}_'
                f'{self.date.day}>{self.slot} | {self.username}'
                f' | <i class="fas fa-user-cog"></i></span>'
            )


class Contact(models.Model):
    """
    Initiates the contact model - kept separate from the user model.
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    telephone = PhoneNumberField(
        null=False,
        blank=False,
        help_text='Include country code, eg +44')
    email = models.EmailField(
        max_length=40,
        blank=False,
        help_text='Email must include "@"')
    message = models.TextField(blank=False, null=False)
    replied = models.IntegerField(choices=REPLIED, default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
