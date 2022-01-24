from django.test import TestCase


class TestViews(TestCase):

    def test_get_awaiting_reg_page(self):
        response = self.client.get('/awaiting_reg/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/awaiting_reg.html')

    def test_sign_up_view(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/account/signup.html')
