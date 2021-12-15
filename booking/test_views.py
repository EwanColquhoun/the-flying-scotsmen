from datetime import date
import json
from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.shortcuts import reverse
from accounts.models import CustomUser
from booking.models import Slot, Aircraft, Booking
from .forms import BookingForm, ContactForm
from .views import EditDisplay


class TestViews(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='testUser', email='test@email.com', password='')
        self.user.set_password('secret')
        self.user.save()
        self.client = Client()
        self.client.login(username='testUser', password='secret')
        self.slot = Slot.objects.create(slot= '0700-0900', start= '07:00', duration= '02:00')
        self.slot2 = Slot.objects.create(slot= '0900-1100', start= '09:00', duration= '02:00')
        self.aircraft = Aircraft.objects.create(reg= 'G-TEST', desc= 'form test')
        # self.test_booking = Booking.objects.create(date= '2024-01-01', slot= self.slot, aircraft= self.aircraft, )

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
        test_booking = Booking.objects.create(date= '2024-01-01', slot= self.slot, aircraft= self.aircraft, )
        response = self.client.get(f'/edit/{test_booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')

    def test_can_make_booking(self):
        test_booking = Booking.objects.create(date= '2024-01-01', slot= self.slot, aircraft= self.aircraft, )
        response = self.client.post('/bookings/', {'date': '2024-01-01', 'slot': '0', 'aircraft': 'G-TEST',})
        existing_booking = Booking.objects.filter(id=test_booking.id)
        self.assertEqual(len(existing_booking), 1)

    def test_can_delete_booking(self):
        test_booking = Booking.objects.create(date= '2024-01-01', slot= self.slot, aircraft= self.aircraft, )
        response = self.client.get(f'/delete/{test_booking.id}')
        self.assertRedirects(response, '/bookings/')
        existing_booking = Booking.objects.filter(id=test_booking.id)
        self.assertEqual(len(existing_booking), 0)


# below tests are experiments to get a test for if showing if the edit page redirects to bookings (EDIT SUCCESS) or edit page(EDIT FAILED). 


# class TestEditView(TestCase):

#     def setUp(self):
#         self.user = CustomUser.objects.create(username='testUser', email='test@email.com', password='')
#         self.user.set_password('secret')
#         self.user.save()
#         self.client = Client()
#         self.client.login(username='testUser', password='secret')
#         self.slot = Slot.objects.create(slot= '0700-0900', start= '07:00', duration= '02:00')
#         self.slot2 = Slot.objects.create(slot= '0900-1100', start= '09:00', duration= '02:00')
#         self.aircraft = Aircraft.objects.create(reg= 'G-TEST', desc= 'form test')

#     def test_edit_view(self):
#         test_booking = Booking.objects.create(date='2024-01-01', slot=self.slot, aircraft=self.aircraft, )
#         request = RequestFactory().post(f'/edit/{test_booking.id}', {'date': '2024-01-01', 'slot': '0900-1100', 'aircraft': 'G-TEST',})
#         print(request)
#         view = EditDisplay()
#         view.setup(request)
#         view.post(request, test_booking.id)
#         self.assertRedirects(request, '/bookings/')


    # def test_can_edit_booking(self):
    #     data = {'date': '2024-01-01', 'slot': '0900-1100', 'aircraft': 'G-TEST',}
    #     test_booking = Booking.objects.create(date='2024-01-01', slot=self.slot, aircraft=self.aircraft, )
    #     print(test_booking.slot)
    #     # response = self.client.get(f'/edit/{test_booking.id}')
    #     response = self.client.post(f'/edit/{test_booking.id}', data=data)
    #     print(response)
    #     # up_booking = get_object_or_404(Booking, id=test_booking.id)
    #     print(test_booking.slot)
    #     self.assertRedirects(response, '/bookings/')
    #     # self.assertEqual(new_response.status_code, 200)
    #     # updated_booking = Booking.objects.get(id= test_booking.id)
    #     # print(test_booking.slot)
    #     # print(updated_booking.slot)
    #     # self.assertFalse(updated_booking.slot, self.slot2)


