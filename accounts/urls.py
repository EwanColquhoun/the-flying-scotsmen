from django.urls import path, re_path
# from django.views.generic import RedirectView
from allauth.account.views import LoginView

from .views import AwaitingRegDisplay, CustomSignUpView

urlpatterns = [
    re_path(r'awaiting_reg/', AwaitingRegDisplay.as_view(), name='awaiting_reg'),
    path('accounts/signup/', CustomSignUpView.as_view(), name='account_signup'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
]
