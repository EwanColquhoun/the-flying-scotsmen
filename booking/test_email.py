from django.test import TestCase
from django.core import mail
from django.test.client import Client
from accounts.models import CustomUser
from .models import Slot, Booking, Contact, Aircraft
from .forms import ContactForm
from .email import send_contact_email_to_admin
import smtplib, ssl
import os

class TestEmailUtil(TestCase):

    def test_send_contact_email(self):
        contact = Contact.objects.create(name='Joe', telephone='123456789', email='joe@tfs.com', message='Test contact message')
        send_contact_email_to_admin(contact)
        self.assertIn('Joe', send_contact_email_to_admin.message)


# below test passes but only tests that the contact data is sent to below email- not really a test for the email.py

# class EmailTest(TestCase):
#     def test_send_contact_email(self):
#         # Send message.
#         contact = Contact.objects.create(name='Joe', telephone='123456789', email='joe@tfs.com', message='Test contact message')
#         mail.send_mail(
#             'Contact Request', contact.message,
#             contact.email, ['to@example.com'],
#             fail_silently=False,
#         )

#         # Test that one message has been sent.
#         self.assertEqual(len(mail.outbox), 1)

#         # Verify that the subject of the first message is correct.
#         self.assertEqual(mail.outbox[0].subject, 'Contact Request')
#         self.assertEqual(mail.outbox[0].body, 'Test contact message')