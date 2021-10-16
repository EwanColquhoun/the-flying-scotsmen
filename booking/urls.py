from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeDisplay.as_view(), name='home'),
    path('bookings/', views.BookingDisplay.as_view(), name='bookings'),
]