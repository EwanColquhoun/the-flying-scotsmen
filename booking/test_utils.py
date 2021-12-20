from django.test import TestCase
from django.test.client import Client
from accounts.models import CustomUser
from .models import Slot, Booking, Contact, Aircraft
from .utils import ValidateBooking
from .forms import BookingForm


class TestValidateBookingUtil(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='testUser', email='test@email.com', password='')
        self.user.set_password('secret')
        self.user.save()
        self.client = Client()
        self.client.login(username='testUser', password='secret')
        self.slot = Slot.objects.create(slot= '0700-0900', start= '07:00', duration= '02:00')
        self.aircraft = Aircraft.objects.create(reg= 'G-TEST', desc= 'form test')
        self.booking = Booking.objects.create(date='2024-01-01', slot=self.slot, aircraft=self.aircraft,)

# not sure how to test this??
    def test_booking_validation(self):
        q_s = 0
        maint = 0
        edit = False
        booking = self.booking
        booking_form = BookingForm(user= Client, data= {'date': '2024/01/01', 'slot': '0', 'aircraft': 'G-TEST' })
        
        ValidateBooking(edit, booking_form, request, msg, booking).booking_validation(request, q_s, maint)