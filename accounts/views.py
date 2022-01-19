from django.shortcuts import render
from django.views import View
from django.contrib import messages
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse
from booking.email import send_register_email_to_admin
from theFlyingScotsmen import settings
from booking.utils import UserMessages


class AwaitingRegDisplay(View):
    """
    Displayed when a registration has been completed but the user is not yet registered.
    """
    def get(self, request):

        return render(
            request,
            'booking/awaiting_reg.html',
        )


class CustomSignUpView(SignupView):
    """
    Overides the default (AllAuth) signup methods.
    """
    success_url = 'awaiting_reg'

    def form_valid(self, form):
        # By assigning the User to a property on the view, we allow subclasses
        # of SignupView to access the newly created User instance
        self.user = form.save(self.request)
        try:
            send_register_email_to_admin(form.instance)
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
        except ImmediateHttpResponse as e:
            return e.response
