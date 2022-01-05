from django.test import TestCase
# from django.core import mail
from django.test.client import Client
from accounts.models import CustomUser
from .models import Slot, Booking, Contact, Aircraft
# from .forms import ContactForm
from .email import send_contact_email_to_admin, send_email_to_admin, send_register_email_to_admin
# import smtplib, ssl
# import os


class TestEmailUtil(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='testUser', email='test@email.com', password='')
        self.user.set_password('secret')
        self.user.save()
        self.client = Client()
        self.client.login(username='testUser', password='secret')
        self.slot = Slot.objects.create(slot='0700-0900', start='07:00', duration='02:00')
        self.aircraft = Aircraft.objects.create(reg='G-TEST', desc='form test')
        self.booking = Booking.objects.create(date='2024-01-01', slot=self.slot, aircraft=self.aircraft, )

    def test_send_contact_email(self):
        contact = Contact.objects.create(name='Joe', telephone='123456789', email='joe@tfs.com', message='Test contact message')
        send_contact_email_to_admin(contact)
        only_contact = Contact.objects.filter(name='Joe')
        self.assertEqual(len(only_contact), 1)

    def test_send_email_to_admin(self):
        booking = self.booking
        send_email_to_admin(booking)
        only_booking = Booking.objects.filter(date='2024-01-01')
        self.assertEqual(len(only_booking), 1)

    def test_send_register_email_to_admin(self):
        user = self.client
        user.username = 'testUser'
        user.first_name = 'Pilot'
        user.last_name = 'Awesome'
        user.email = 'ap@tfs.com'
        user.message = 'Please accept me'
        
        send_register_email_to_admin(user)
        name = self.user.username
        self.assertEqual(name, 'testUser')

# below test passes but only tests that the contact data is sent to below email- not really a test for the email.py

# class EmailTest(TestCase):
#     def test_send_contact_email(self):
#         # Send message.
#         contact = Contact.objects.create(name='Joe', telephone='123456789', email='joe@tfs.com', message='Test contact message')
#         mail.send_mail(
#             'Contact Request', contact.message,
#             contact.email, ['Joe@example.com'],
#             fail_silently=False,
#         )

#         # Test that one message has been sent.
#         self.assertEqual(len(mail.outbox), 1)

#         # Verify that the subject of the first message is correct.
#         self.assertEqual(mail.outbox[0].subject, 'Contact Request')
#         self.assertEqual(mail.outbox[0].body, 'Test contact message')