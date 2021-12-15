from datetime import date
from django.test import TestCase
from django.test.client import Client
from accounts.models import CustomUser
from booking.models import Slot, Aircraft, Booking
from .forms import BookingForm, ContactForm


class TestViews(TestCase):

    def setUp(self):
        self.slot = Slot.objects.create(slot= '0700-0900', start= '07:00', duration= '02:00')
        self.aircraft = Aircraft.objects.create(reg= 'G-TEST', desc= 'form test')
        self.test_booking = Booking.objects.create(date= '2024-01-01', slot= self.slot, aircraft= self.aircraft, )

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/index.html')

    def test_get_bookings_page(self):
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/bookings.html')

    def test_get_calendar_page(self):
        response = self.client.get('/calendar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/calendar.html')

    def test_get_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/contact.html')
    
    def test_get_edit_booking_page(self):
        response = self.client.get(f'/edit/{self.test_booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')

    def test_can_edit_booking(self):
        test_booking = Booking.objects.create(date= '2024-01-01', slot= self.slot, aircraft= self.aircraft, )
        response = self.client.post(f'/edit/{test_booking.id}', {'date': '2024-01-02',})
        self.assertRedirects(response, '/bookings/')
        updated_booking = Booking.objects.get(date='2024-01-02')
        self.assertFalse(updated_booking.date)

    # def test_can_make_booking(self):
    #     response = self.client.post('/bookings/', {'date': '2024-01-01', 'slot': '0', 'aircraft': 'G-TEST',})
    #     self.assertRedirects(response, '/bookings/')

    def test_can_delete_booking(self):
        response = self.client.get(f'/delete/{self.test_booking.id}')
        self.assertRedirects(response, '/bookings/')
        existing_booking = Booking.objects.filter(id=self.test_booking.id)
        self.assertEqual(len(existing_booking), 0)


