from django.test import TestCase, RequestFactory
from .views import CustomSignUpView
from .forms import CustomSignUpForm


class TestViews(TestCase):

    def test_get_awaiting_reg_page(self):
        response = self.client.get('/awaiting_reg/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/awaiting_reg.html')

    def test_sign_up_view(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/account/signup.html')

# class TestCustomSignUpView(TestCase):

#     def test_form_valid(self):
#         data = {'username': 'joeybloggs', 'first_name':'joe', 'last_name':'bloggs', 'email':'jb@tfs.com', 'password1':'secret11', 'password2':'secret11', 'message':'test'}
#         form = CustomSignUpForm(data)
#         request = RequestFactory().post('/accounts/signup/', data=data)
#         view = CustomSignUpView()
#         view.setup(request)
#         view.form_valid(form)(request)
#    
