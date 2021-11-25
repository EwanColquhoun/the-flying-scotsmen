from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import calendar
from .models import Booking, Contact
from .forms import BookingForm, ContactForm, SignUpForm, UserMessageForm
from .utils import Calendar
from .email import send_email_to_admin, send_contact_email_to_admin, send_register_email_to_admin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import login, authenticate


def validate_booking(booking_form, request, msg, booking, *args, **kwargs):
    today = date.today()
    message = request.POST.get('notes')

    if booking_form.instance.date > today:
        print('today')
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
        if booking_form.instance.slot_id==12 and request.user.username != 'admin2021':
            print('maint')
            messages.add_message(request, messages.WARNING, 'Only Admin can book MAINT slots. Thank you.')
            # redirect('edit_booking', booking)
        else:
            if edit:
                if qs != 0 and message != msg and maint == 0: #allows a booking to be changed but only if the msg is changed. need to work on this , maybe another if else or elif statement.
                    print('legit! with a changed message')
                    booking = booking_form.save(commit=False)
                    booking.save()
                    send_email_to_admin(booking_form.instance)
                    messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by Admin. Thank you.')
            elif qs == 0 and maint == 0:
                print('legit with the same message, or new booking')
                booking = booking_form.save(commit=False)
                booking.save()
                send_email_to_admin(booking_form.instance)
                messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by Admin. Thank you.')
            elif qs != 0 and maint !=0:
                print('bookings today=', qs, 'maint=', maint, )
                messages.add_message(request, messages.ERROR, 'That aircraft is on MAINT, please check date/slot and aircraft and try again. Thank you.')
                # redirect('edit_booking', booking)
            else:
                print('double booking')
                messages.add_message(request, messages.ERROR, 'This is a double booking, please check date/slot and aircraft and try again. Thank you.')
    else:
        print('nottoday')
        messages.add_message(request, messages.WARNING, 'Booking dates must be in the future, please check the date. Thank you.')
        # redirect('edit_booking', booking)


class HomeDisplay(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'booking/index.html',
        )


class AwaitingRegDisplay(View):

    def get(self, request, *args, **kwargs):
        
        return render(
            request,
            'booking/awaiting_reg.html',
        )


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
        edit = False
        current_user = request.user
        booking_form = BookingForm(data=request.POST, user=request.user)
        bookings = Booking.objects.filter(username=current_user, approved=True)


        if booking_form.is_valid():
            validate_booking(edit, booking_form, request, bookings, current_user)
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
        edit = True
        current_user = request.user
        booking = get_object_or_404(Booking, id=booking_id)
        msg = booking.notes
        bookings = Booking.objects.filter(username=current_user, approved=True)
        today = date.today()
        booking_form = BookingForm(request.POST, instance=booking, user=request.user)

        if booking_form.is_valid():
            validate_booking(edit, booking_form, request, msg, booking, current_user, booking.id)
            return redirect ('bookings')
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

    def get(self, request, *args, **kwargs):
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
    def deleteBooking(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Your Booking has been deleted successfully. Thank you.')
        return HttpResponseRedirect(reverse('calendar'))


class ContactDisplay(View):
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'contact_form': form,
        }
        return render(
            request,
            'booking/contact.html',
            context
        )

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.replied = False
            form.save()
            send_contact_email_to_admin(form.instance)
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent, we will endeavour to reply as soon as we can. Thank you.')
            return redirect('contact')
        else: 
            messages.add_message(request, messages.WARNING, 'All fields are required, please check the details and try again. Thank you.')
            return redirect('contact')

        form = ContactForm()
        context = {
            'contact_form': form,
        }
        return render(request, 'booking/contact.html', context)


class SignUpDisplay(View):

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        # message_form = UserMessageForm()
        login_url = reverse("account_login")
        return render(
            request,
            'account/signup.html',
            {
                'form': form,
                # 'msgform': message_form,
                "login_url": login_url,
            }
        )

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        # message_form = UserMessageForm(request.POST.get('message'))
        if form.is_valid():
            form.save()
            # message_form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # message = message_form.cleaned_data.get('message')
            user = authenticate(username=username, password=raw_password)
            # print(user.registered.message)
            login(request, user)
            send_register_email_to_admin(form.instance)
            messages.add_message(request, messages.SUCCESS, 'Your request to register has been noted. We will be in touch shortly. Thank you.')
            return redirect('awaiting_reg')
        else:
            form = SignUpForm()
            messages.add_message(request, messages.WARNING, 'All fields are required, please check the details and try again. Thank you.')
            return redirect('account_signup')
            # return render(request, 'account/signup.html', {'form': form,})
