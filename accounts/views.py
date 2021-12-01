from django.shortcuts import render
from django.views import View
from allauth.account.views import SignupView


class AwaitingRegDisplay(View):

    def get(self, request):

        return render(
            request,
            'booking/awaiting_reg.html',
        )


# class CustomSignUp(SignupView):
#     success_url = 'awaiting_reg'

#     def get_success_url(self):
#         # Explicitly passed ?next= URL takes precedence
#         ret = (success_url
#             # get_next_redirect_url(self.request, self.redirect_field_name)
#             # or self.success_url
#         )
#         return ret