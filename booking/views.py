from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.utils.safestring import mark_safe
import calendar
from .models import Booking
from .forms import BookingForm
from .utils import Calendar
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

    @staticmethod
    def editBooking(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        if request.method == 'POST':
            booking_form = BookingForm(request.POST, instance=booking)
            if booking_form.is_valid():
                qs = Booking.objects.filter(
                    date=booking_form.instance.date,
                    slot=booking_form.instance.slot,
                    aircraft_id=booking_form.instance.aircraft_id,
                ).count()

            if qs == 0:
                booking_form.save()
                messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by admin. Thank you.')
                return redirect('bookings')
            else:
                messages.add_message(request, messages.WARNING, 'This is a double booking, please check date/slot and aircraft and try again. Thank you.')
                return redirect('bookings')

        booking_form = BookingForm(instance=booking)
        context = {
            'form': booking_form,
            'booking': booking,
        }
        return render(request, "booking/edit_booking.html", context)

    @staticmethod
    def deleteBooking(request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect('bookings')


class CalendarView(generic.ListView):
    model = Booking
    template_name = 'booking/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = self.get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        bookings = Booking.objects.filter(approved=True)
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


    # def event(self, request, event_id=None):
    #     instance = Booking()
    #     if event_id:
    #         instance = get_object_or_404(Booking(), pk=event_id)
    #     else:
    #         instance = Booking()

    #     form = BookingForm(request.POST or None, instance=instance)
    #     if request.POST and form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('booking:calendar'))
    #     return render(request, 'booking/booking.html', {'form': form, 'booking': instance})


class ContactDisplay(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'booking/contact.html',
        )