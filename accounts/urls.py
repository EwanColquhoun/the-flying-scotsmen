from django.urls import path

from allauth.account.views import LoginView

from .views import AwaitingRegDisplay

urlpatterns = [
    path('awaiting-reg', AwaitingRegDisplay.as_view(), name='awaiting_reg'),
    # path('accounts/signup/', SignUpDisplay.as_view(), name='account_signup'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
]
