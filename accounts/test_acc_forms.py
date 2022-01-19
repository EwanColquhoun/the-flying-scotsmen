from django.test import TestCase
from .forms import CustomSignUpForm


class TestCustomSignUpForm(TestCase):

    def test_form_validated(self):
        form = CustomSignUpForm({'username': 'EwanCol',
                                 'first_name': 'Ewan',
                                 'last_name': 'Col',
                                 'email': 'testemail@tfs.com',
                                 'password1': 'testPassword01',
                                 'password2': 'testPassword01',
                                 'message': 'Test message'})
        self.assertTrue(form.is_valid())

    def test_username_required(self):
        form = CustomSignUpForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0],
                         'This field is required.')

    def test_first_name_required(self):
        form = CustomSignUpForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')

    def test_last_name_required(self):
        form = CustomSignUpForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')

    def test_email_required(self):
        form = CustomSignUpForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_message_required(self):
        form = CustomSignUpForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0],
                         'This field is required.')
