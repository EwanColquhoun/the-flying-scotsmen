from django.test import TestCase, RequestFactory
from django.test.client import Client
from accounts.models import CustomUser
from .models import Slot, Booking, Aircraft
from .views import BookingDisplay


class TestValidateBookingUtil(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            username='testUser', email='test@email.com', password='')
        self.user.set_password('secret')
        self.user.save()
        self.client = Client()
        self.client.login(username='testUser', password='secret')
        self.slot = Slot.objects.create(
            slot='0700-0900', start='07:00', duration='02:00')
        self.aircraft = Aircraft.objects.create(
            reg='G-TEST', desc='form test')
        self.booking = Booking.objects.create(
            date='2024-01-01', slot=self.slot, aircraft=self.aircraft,)
        self.factory = RequestFactory()

    def test_booking_validation(self):
        request = self.factory.post('/bookings/')
        request.user = self.user
        response = BookingDisplay.as_view()(request)
        self.assertEqual(response.status_code, 200)
