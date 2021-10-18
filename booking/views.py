import datetime
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Booking, Aircraft
from .forms import BookingForm
# from django.http import HttpResponseRedirect
from django.contrib import messages


# class BookingList(generic.ListView):
#     model = Aircraft
#     queryset = Aircraft.objects.all()
#     template_name = 'index.html'


class HomeDisplay(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'booking/index.html',
            {
                'datetime': datetime,
            }
        )


class BookingDisplay(View):

    def get(self, request, *args, **kwargs):
        current_user = request.user
        bookings = Booking.objects.filter(username=current_user).filter(approved=True)

        return render(
            request,
            'booking/bookings.html',
            {
                "bookings": bookings,
                "bookingform": BookingForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        current_user = request.user
        booking_form = BookingForm(data=request.POST)
        bookings = Booking.objects.filter(username=current_user, approved=True)

        if booking_form.is_valid():
            qs = Booking.objects.filter(
                date=booking_form.instance.date,
                slot=booking_form.instance.slot,
                aircraft_id=booking_form.instance.aircraft_id,
            ).count()

            if qs == 0:
                booking = booking_form.save(commit=False)
                booking.save()
                messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by admin. Thank you.')
                return redirect('bookings')
            else:
                messages.add_message(request, messages.WARNING, 'This is a double booking, please check date/slot and aircraft and try again. Thank you.')
                return redirect('bookings')
        else:
            booking_form = BookingForm()
    
        return render(
            request,
            'booking/bookings.html',
            {
                "bookings": bookings,
                "bookingform": BookingForm(),
            },
        )


class CalendarDisplay(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'booking/calendar.html',
        )


class ContactDisplay(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'booking/contact.html',
        )
