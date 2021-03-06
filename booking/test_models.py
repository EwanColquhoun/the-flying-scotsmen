from django.test import TestCase
from .models import Slot, Booking, Contact, Aircraft


class TestModels(TestCase):

    def setUp(self):
        self.slot = Slot.objects.create(
            slot='0700-0900', start='07:00', duration='02:00')
        self.aircraft = Aircraft.objects.create(reg='G-TEST', desc='form test')

    def test_slot_admin_option_is_false(self):
        slot = Slot.objects.create(
            slot='1200-1400', start='12:00', duration='02:00')
        self.assertFalse(slot.admin)
        slot_list = Slot.objects.all()
        self.assertEqual(len(slot_list), 2)

    def test_booking_approved_option_false(self):
        booking = Booking.objects.create(
            date='2024-01-01', slot=self.slot, aircraft=self.aircraft,)
        self.assertFalse(booking.approved)
        booking_list = Booking.objects.all()
        self.assertEqual(len(booking_list), 1)

    def test_contact_default_replied_false(self):
        contact = Contact.objects.create(
            name='Joe', telephone='123456789',
            email='joe@tfs.com', message='Test contact message')
        self.assertFalse(contact.replied)
        contact_list = Contact.objects.all()
        self.assertEqual(len(contact_list), 1)
