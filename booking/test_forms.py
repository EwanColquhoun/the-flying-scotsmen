from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from accounts.models import CustomUser
from booking.models import Slot, Aircraft
from .forms import BookingForm, ContactForm


class TestContactForm(TestCase):

    def test_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_telephone_is_required(self):
        form = ContactForm({'name': 'John', 'telephone':''})
        self.assertFalse(form.is_valid())
        self.assertIn('telephone', form.errors.keys())
        self.assertEqual(form.errors['telephone'][0], 'This field is required.')
    
    def test_email_is_required(self):
        form = ContactForm({'name': 'John', 'telephone':'12345678910', 'email':''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_message_is_required(self):
        form = ContactForm({'name': 'John', 'telephone':'12345678910', 'email':'john@john.com', 'message':''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, ('name', 'telephone', 'email', 'message'))


class TestBookingForm(TestCase):

    def setUp(self): 
        self.user = CustomUser.objects.create(username='testUser', email='test@email.com', password='')
        self.user.set_password('secret')
        self.user.save()
        self.client = Client()
        self.client.login(username='testUser', password='secret')
        self.slot = Slot.objects.create(slot= '0700-0900', start= '07:00', duration= '02:00')
        self.aircraft = Aircraft.objects.create(reg= 'G-TEST', desc= 'form test')

    def test_slot_is_required(self):
        form = BookingForm(user= Client, data= {'date': '2024/01/01', 'slot': '', 'aircraft': '0' })
        self.assertFalse(form.is_valid())
        self.assertIn('slot', form.errors.keys())
        self.assertEqual(form.errors['slot'][0], 'This field is required.')

    def test_aircraft_is_required(self):
        form = BookingForm(user= Client, data= {'date': '2024/01/01', 'slot': '0', 'aircraft': '' })
        self.assertFalse(form.is_valid())
        self.assertIn('aircraft', form.errors.keys())
        self.assertEqual(form.errors['aircraft'][0], 'This field is required.')

    def test_date_is_required(self):
        form = BookingForm(user= Client, data= {'date': '', 'slot': '0', 'aircraft': '0' })
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')
