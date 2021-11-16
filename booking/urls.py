from . import views
from django.urls import path
from django.conf.urls import re_path

urlpatterns = [
    path('', views.HomeDisplay.as_view(), name='home'),
    path('bookings/', views.BookingDisplay.as_view(), name='bookings'),
    path('contact/', views.ContactDisplay.as_view(), name='contact'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    # path('edit/<booking_id>', views.BookingDisplay.editBooking, name='edit_booking'),
    path('edit/<booking_id>', views.EditDisplay.as_view(), name='edit_booking'),
    path('delete/<booking_id>', views.BookingDisplay.deleteBooking, name='delete_booking'),
]