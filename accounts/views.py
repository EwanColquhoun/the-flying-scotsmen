import sys
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse
from booking.email_util import register_email
from booking.utils import UserMessages
from theFlyingScotsmen import settings


class AwaitingRegDisplay(View):
    """
    Displayed when a registration has been completed
    but the user is not yet registered.
    """
    def get(self, request):
        return render(
            request,
            'account/awaiting_reg.html',
        )


class CustomSignUpView(SignupView):
    """
    Overides the default (AllAuth) signup methods.
    """
    success_url = 'awaiting_reg'

    def form_valid(self, form):
        # User initiated here to gain access.
        self.user = form.save(self.request)
        try:
            if 'runserver' in sys.argv:
                messages.add_message(
                    self.request,
                    messages.SUCCESS,
                    UserMessages.register)
                return complete_signup(
                    self.request,
                    self.user,
                    settings.EMAIL_VERIFICATION_DEV,
                    self.success_url,
                )
            else:
                register_email(form.instance)
                messages.add_message(
                    self.request,
                    messages.SUCCESS,
                    UserMessages.register)
                return complete_signup(
                    self.request,
                    self.user,
                    settings.EMAIL_VERIFICATION,
                    self.success_url,
                )
        except ImmediateHttpResponse as error:
            return error.response
