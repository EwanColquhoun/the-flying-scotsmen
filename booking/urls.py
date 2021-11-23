from . import views
from django.urls import path
from django.conf.urls import re_path

from allauth.account.views import LoginView

urlpatterns = [
    path('', views.HomeDisplay.as_view(), name='home'),
    path('bookings/', views.BookingDisplay.as_view(), name='bookings'),
    path('contact/', views.ContactDisplay.as_view(), name='contact'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    path('edit/<booking_id>', views.EditDisplay.as_view(), name='edit_booking'),
    path('delete/<booking_id>', views.BookingDisplay.deleteBooking, name='delete_booking'),
    path('delete_calendar_booking/<booking_id>', views.CalendarView.deleteBooking, name='delete_calendar_booking'),
    path('awaiting-reg', views.AwaitingRegDisplay.as_view(), name='awaiting_reg'),
    path('accounts/signup/', views.SignUpDisplay.as_view(), name='account_signup'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
]