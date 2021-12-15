from django.test import TestCase
from .models import Slot, Booking, Contact


class TestModels(TestCase):

    def test_slot_admin_option_is_false(self):
        slot = Slot.objects.create(slot='1200-1400', start='12:00', duration='02:00')
        self.assertFalse(slot.admin)