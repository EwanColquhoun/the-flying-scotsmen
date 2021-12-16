from django.test import TestCase
from django.test.client import Client
from .models import Group_Member, CustomUser


class TestAccModels(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='testUser', email='test@email.com', password='', message='Test message')
        self.user.set_password('secret')
        self.user.save()
        self.client = Client()
        self.client.login(username='testUser', password='secret')

    def test_group_member_registered_is_false(self):
        test_member = Group_Member.objects.create(user=self.user)
        self.assertFalse(test_member.registered)

    def test_group_member_message_is_accepted(self):
        member_message = CustomUser.objects.get(message='Test message')
        print(member_message.message)
        self.assertTrue(member_message, 'Test message')
