from datetime import date, timedelta
from django.contrib import messages
from calendar import HTMLCalendar
from .models import Booking
from .email import send_contact_email_to_admin, send_email_to_admin, send_register_email_to_admin


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(date__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li class="event"> {event.get_html_url} </li>'

        if day:
            if day != 0 and len(events_per_day) == 10:
                return f"<td class='day-full'><a class='btn date' data-bs-toggle='modal' data-bs-target='#myModal' name={self.month}_{day}>{day}</a><ul class='booking_list'> {d} </ul></td>"
            elif day != 0 and len(events_per_day) >= 1 and len(events_per_day) <= 9:
                return f"<td class='day-medium'><a class='btn date' data-bs-toggle='modal' data-bs-target='#myModal' name={self.month}_{day}>{day}</a><ul class='booking_list'> {d} </ul></td>"
            else:
                return f"<td class='day-free'><a class='btn date' data-bs-toggle='modal' data-bs-target='#myModal' name={self.month}_{day}>{day}</a><ul class='booking_list'> {d} </ul></td>"
        else:
            return '<td class="day-null day"></td>'


    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Booking.objects.filter(date__year=self.year, date__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal


def passthrough_next_redirect_url(request, url, redirect_field_name):
    assert url.find("?") < 0  # TODO: Handle this case properly
    next_url = get_next_redirect_url(request, redirect_field_name)
    if next_url:
        url = url + "?" + urlencode({redirect_field_name: next_url})
    return url


class Validate_booking:
    def __init__(self, edit, booking_form, request, msg, booking):

        self.edit = edit
        self.booking_form = booking_form
        self.request = request
        self.msg = msg
        self.booking = booking
        self.today = date.today()
        self.message = self.request.POST.get('notes')

    def edit_validation(self, request, qs, maint):
        if qs != 0 and self.message != self.msg and maint == 0:
            booking = self.booking_form.save(commit=False)
            booking.save()
            send_email_to_admin(self.booking_form.instance)
            messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by Admin. Thank you.')
            return True
        elif qs == 0 and maint == 0:
            booking = self.booking_form.save(commit=False)
            booking.save()
            send_email_to_admin(self.booking_form.instance)
            messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by Admin. Thank you.')
            return True
        elif qs != 0 and maint != 0:
            messages.add_message(request, messages.ERROR, 'That aircraft is on MAINT, please check date/slot and aircraft and try again. Thank you.')
            return False
        else:
            messages.add_message(request, messages.ERROR, 'This is a double booking, please check date/slot and aircraft and try again. Thank you.')
            return False
            
    def booking_validation(self, request, qs, maint):
        if qs == 0 and maint == 0:
            booking = self.booking_form.save(commit=False)
            booking.save()
            send_email_to_admin(self.booking_form.instance)
            messages.add_message(request, messages.SUCCESS, 'Your booking will be added once approved by Admin. Thank you.')
            return True
        elif qs != 0 and maint != 0:
            messages.add_message(request, messages.ERROR, 'That aircraft is on MAINT, please check date/slot and aircraft and try again. Thank you.')
            return False
        else:
            messages.add_message(request, messages.ERROR, 'This is a double booking, please check date/slot and aircraft and try again. Thank you.')
            return False

    def validate(self):
        if self.booking_form.instance.date > self.today:
            qs = Booking.objects.filter(
                    date=self.booking_form.instance.date,
                    slot=self.booking_form.instance.slot,
                    aircraft_id=self.booking_form.instance.aircraft_id,
                    ).count()
            maint = Booking.objects.filter(
                    date=self.booking_form.instance.date,
                    slot=12,
                    aircraft_id=self.booking_form.instance.aircraft_id,
                    ).count()
            if self.booking_form.instance.slot_id == 12 and self.request.user.username != 'admin2021':
                messages.add_message(self.request, messages.WARNING, 'Only Admin can book MAINT slots. Thank you.')
            else:
                if self.edit:
                    updated = self.edit_validation(self.request, qs, maint)
                    return updated
                else:
                    self.booking_validation(self.request, qs, maint)
        else:
            messages.add_message(request, messages.WARNING, 'Booking dates must be in the future, please check the date. Thank you.')

