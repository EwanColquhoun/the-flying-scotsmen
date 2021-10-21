from . import views
from django.urls import path
from django.conf.urls import re_path

urlpatterns = [
    path('', views.HomeDisplay.as_view(), name='home'),
    path('bookings/', views.BookingDisplay.as_view(), name='bookings'),
    # path('calendar/', views.CalendarView().as_view(), name='calendar'),
    path('contact/', views.ContactDisplay.as_view(), name='contact'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.CalendarView.event, name='event_new'),
	re_path(r'^event/edit/(?P<event_id>\d+)/$', views.CalendarView.event, name='event_edit'),
]