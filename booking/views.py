from datetime import datetime, timedelta, date
import calendar
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.utils.safestring import mark_safe
from django.contrib import messages

from .models import Booking
from .forms import BookingForm, ContactForm
from .utils import Calendar, ValidateBooking, UserMessages
from .email import send_contact_email_to_admin


class HomeDisplay(View):
    """
    The home page
    """
    def get(self, request):

        return render(
            request,
            'booking/index.html',
        )


class BookingDisplay(View):
    """
    Bookings page
    """

    def get(self, request):
        current_user = request.user
        bookings = Booking.objects.filter(username=current_user)

        return render(
            request,
            'booking/bookings.html',
            {
                "bookings": bookings,
                "bookingform": BookingForm(user=request.user),
            },
        )

    def post(self, request):
        edit = False
        current_user = request.user
        booking_form = BookingForm(data=request.POST, user=request.user)
        bookings = Booking.objects.filter(username=current_user, approved=True)

        if booking_form.is_valid():
            ValidateBooking(
                edit,
                booking_form,
                request, bookings,
                current_user).validate()
            return redirect('bookings')
        else:
            booking_form = BookingForm(user=request.user)

        return render(
            request,
            'booking/bookings.html',
            {
                "bookings": bookings,
                "bookingform": BookingForm(user=request.user),
            },
        )

    @staticmethod
    def delete_booking(request, booking_id):
        """
        Deletes the booking when called, returns the user to
        bookings with a confirmation message.
        """
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.add_message(request, messages.SUCCESS, UserMessages.deleted)
        return HttpResponseRedirect(reverse('bookings'))


class EditDisplay(View):
    """
    Edit booking page
    """
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking_form = BookingForm(instance=booking, user=request.user)
        return render(
            request,
            'booking/edit_booking.html',
            {
                "form": booking_form,
                'booking': booking,
            },
        )

    def post(self, request, booking_id):
        edit = True
        current_user = request.user
        booking = get_object_or_404(Booking, id=booking_id)
        msg = booking.notes
        bookings = Booking.objects.filter(username=current_user, approved=True)
        booking_form = BookingForm(
            request.POST,
            instance=booking,
            user=request.user)

        if booking_form.is_valid():
            updated = ValidateBooking(
                edit,
                booking_form,
                request,
                msg,
                booking).validate()
            if updated:
                return redirect('bookings')
            else:
                return redirect('edit_booking', booking_id=booking.id)

        else:
            booking_form = BookingForm(user=request.user)

        return render(
            request,
            'booking/edit_booking.html',
            {
                "bookings": bookings,
                "form": booking_form,
            },
        )


class CalendarView(View):
    """
    Calendar page
    """

    def get(self, request):
        d = self.get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        bookings = Booking.objects.all()
        return render(request,
                      'booking/calendar.html',
                      {
                        'calendar': mark_safe(html_cal),
                        'prev_month': self.prev_month(d),
                        'next_month': self.next_month(d),
                        'bookings': bookings,
                       })

    def get_date(self, req_month):
        if req_month:
            year, month = (int(x) for x in req_month.split('-'))
            return date(year, month, day=1)
        return datetime.today()

    def prev_month(self, d):
        first = d.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
        return month

    def next_month(self, d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
        return month

    @staticmethod
    def delete_booking(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.add_message(request, messages.SUCCESS, UserMessages.deleted)
        return HttpResponseRedirect(reverse('calendar'))


class ContactDisplay(View):
    """
    Displays the contact page.
    """

    def get(self, request):
        form = ContactForm()
        context = {
            'contact_form': form,
        }
        return render(
            request,
            'booking/contact.html',
            context
        )

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.replied = False
            form.save()
            send_contact_email_to_admin(form.instance)
            messages.add_message(
                request,
                messages.SUCCESS,
                UserMessages.sent)
            return redirect('contact')
        else:
            messages.add_message(
                request,
                messages.WARNING,
                UserMessages.errors)
            return redirect('contact')

        form = ContactForm()
        context = {
            'contact_form': form,
        }
        return render(request, 'booking/contact.html', context)
