from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import calendar
from .models import Booking, Contact
from .forms import BookingForm, ContactForm
from .utils import Calendar
from .email import send_email_to_admin, send_contact_email_to_admin
from django.http import HttpResponseRedirect
from django.contrib import messages


class HomeDisplay(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'booking/index.html',
        )


# class SignUpDisplay(View):

#     def get(self, request, *args, **kwargs):
#         signup_form = 
#         return render(
#             request,
#             'account/signup.html',
#         )
    


def validate_booking(booking_form, request, booking, *args, **kwargs):
    today = date.today()
    if booking_form.instance.date > today:
        qs = Booking.objects.filter(
            date=booking_form.instance.date,
            slot=booking_form.instance.slot,
            aircraft_id=booking_form.instance.aircraft_id,
        ).count()

        maint = Booking.objects.filter(
            date=booking_form.instance.date,
            slot=12,
            aircraft_id=booking_form.instance.aircraft_id,
        ).count()

        if booking_form.instance.slot_id==12:
            messages.add_message(request, messages.WARNING, 'Only Admin can book MAINT slots. Thank you.')
            return redirect('edit_booking', booking)
        else:
            if qs == 0 and maint == 0:
                booking = booking_form.save(commit=False)
                booking.save()
                send_email_to_admin(booking_form.instance)
                messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by admin. Thank you.')
            else:
                messages.add_message(request, messages.WARNING, 'This is a double booking, please check date/slot and aircraft and try again. Thank you.')
                return redirect('edit_booking', booking)

    else:
        messages.add_message(request, messages.WARNING, 'Booking dates must be in the future, please check the date. Thank you.')
        return redirect('edit_booking', booking)


class BookingDisplay(View):

    def get(self, request, *args, **kwargs):
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

    def post(self, request, *args, **kwargs):
        current_user = request.user
        booking_form = BookingForm(data=request.POST, user=request.user)
        bookings = Booking.objects.filter(username=current_user, approved=True)


        if booking_form.is_valid():
            validate_booking(booking_form, request, bookings, current_user)
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
    def deleteBooking(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Your Booking has been deleted successfully. Thank you.')
        return HttpResponseRedirect(reverse('bookings'))


class EditDisplay(View):

    def get(self, request, booking_id):
        current_user = request.user
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
        current_user = request.user
        booking = get_object_or_404(Booking, id=booking_id)
        bookings = Booking.objects.filter(username=current_user, approved=True)
        today = date.today()
        
        if request.method == 'POST':
            booking_form = BookingForm(request.POST, instance=booking, user=request.user)
            if booking_form.is_valid():
                validate_booking(booking_form, request, bookings, current_user, booking.id)
                # return redirect ('bookings')
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


class CalendarView(generic.ListView):
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'booking/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = self.get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        bookings = Booking.objects.all()
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = self.prev_month(d)
        context['next_month'] = self.next_month(d)
        context['bookings'] = bookings
        return context

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
    def deleteBooking(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Your Booking has been deleted successfully. Thank you.')
        return HttpResponseRedirect(reverse('calendar'))



class ContactDisplay(View):
    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        context = {
            'contact_form': contact_form,
        }
        return render(
            request,
            'booking/contact.html',
            context
        )

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(data=request.POST)
        if request.method == 'POST':
            contact_form = ContactForm(data=request.POST)
            if contact_form.is_valid:
                contact_form.replied = False
                contact_form.save()
                send_contact_email_to_admin(contact_form.instance)
                messages.add_message(request, messages.SUCCESS, 'Your message has been sent, we will endeavour to reply as soon as we can. Thank you.')
                return redirect('contact')
            else:
                messages.add_message(request, messages.WARNING, 'This is a double booking, please check date/slot and aircraft and try again. Thank you.')
                return redirect('contact')

        else:
            contact_form = ContactForm()
            context = {
                'contact_form': contact_form,
            }
        return render(request, 'booking/contact.html', context)
    
