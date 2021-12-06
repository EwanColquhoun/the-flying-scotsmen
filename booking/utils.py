from datetime import date
from calendar import HTMLCalendar
from django.contrib import messages
from .models import Booking
from .email import send_email_to_admin


class Calendar(HTMLCalendar):
    """
    Initiates the HTML Calendar
    """
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
                return (f"<td class='day-full'><a class='btn date'"
                        f" data-bs-toggle='modal' data-bs-target='#myModal'"
                        f" name={self.month}_{day}>{day}</a><ul "
                        f"class='booking_list'> {d} </ul></td>"
                        )
            elif ((day != 0) and (len(events_per_day) >= 1) and
                  (len(events_per_day) <= 9)):
                return (f"<td class='day-medium'><a class='btn date'"
                        f" data-bs-toggle='modal' data-bs-target='#myModal'"
                        f" name={self.month}_{day}>{day}</a><ul"
                        f" class='booking_list'> {d} </ul></td>"
                        )
            else:
                return (f"<td class='day-free'><a class='btn date'"
                        F" data-bs-toggle='modal' data-bs-target='#myModal'"
                        f" name={self.month}_{day}>{day}</a><ul"
                        f" class='booking_list'> {d} </ul></td>"
                        )
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
        events = Booking.objects.filter(
            date__year=self.year,
            date__month=self.month)
        cal_inner = ('<table border="0" cellpadding="0"'
                    ' cellspacing="0" class="calendar">')
        cal = f'{cal_inner}\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal


class ValidateBooking:
    """
    Takes the booking information, validates for dates,
    aircraft, slots, no double bookings, correct user for
    the chosen slot.
    """
    def __init__(self, edit, booking_form, request, msg, booking):

        self.edit = edit
        self.booking_form = booking_form
        self.request = request
        self.msg = msg
        self.booking = booking
        self.today = date.today()
        self.message = self.request.POST.get('notes')

    def edit_validation(self, request, q_s, maint):
        """
        Validates on the edit booking page, different as it needs to compare
        the message field aswell.
        """
        if q_s != 0 and self.message != self.msg and maint == 0:
            booking = self.booking_form.save(commit=False)
            booking.save()
            send_email_to_admin(self.booking_form.instance)
            messages.add_message(
                request,
                messages.SUCCESS,
                UserMessages.confirmed)
            return True
        elif q_s == 0 and maint == 0:
            booking = self.booking_form.save(commit=False)
            booking.save()
            send_email_to_admin(self.booking_form.instance)
            messages.add_message(
                request,
                messages.SUCCESS,
                UserMessages.confirmed)
            return True
        elif q_s != 0 and maint != 0:
            messages.add_message(
                request,
                messages.ERROR,
                UserMessages.onMaint)
            return False
        else:
            messages.add_message(
                request,
                messages.ERROR,
                UserMessages.double)
            return False

    def booking_validation(self, request, q_s, maint):
        """
        Validates the initial booking.
        """
        if q_s == 0 and maint == 0:
            booking = self.booking_form.save(commit=False)
            booking.save()
            send_email_to_admin(self.booking_form.instance)
            messages.add_message(
                request,
                messages.SUCCESS,
                UserMessages.confirmed)
            return True
        elif q_s != 0 and maint != 0:
            messages.add_message(
                request,
                messages.ERROR,
                UserMessages.onMaint)
            return False
        else:
            messages.add_message(
                request,
                messages.ERROR,
                UserMessages.double)
            return False

    def validate(self):
        """
        Calls the respective validation methods.
        """
        if self.booking_form.instance.date > self.today:
            q_s = Booking.objects.filter(
                    date=self.booking_form.instance.date,
                    slot=self.booking_form.instance.slot,
                    aircraft_id=self.booking_form.instance.aircraft_id,
                    ).count()
            maint = Booking.objects.filter(
                    date=self.booking_form.instance.date,
                    slot=7,
                    aircraft_id=self.booking_form.instance.aircraft_id,
                    ).count()
            if (self.booking_form.instance.slot_id == 7
               and self.request.user.username != 'admin2021'):
                messages.add_message(
                    self.request,
                    messages.WARNING,
                    UserMessages.maint)
            else:
                if self.edit:
                    updated = self.edit_validation(self.request, q_s, maint)
                    return updated
                else:
                    self.booking_validation(self.request, q_s, maint)
        else:
            messages.add_message(
                self.request,
                messages.WARNING,
                UserMessages.past)


class UserMessages:
    """
    Message variables stored here.
    """

    past = ('Booking dates must be in the future,'
            ' please check the date. Thank you.')
    confirmed = 'Your booking will be added once approved by Admin. Thank you.'
    maint = 'Only Admin can book MAINT slots. Thank you.'
    double = ('This is a double booking, please check date/slot and'
              ' aircraft and try again. Thank you.')
    onMaint = ('That aircraft is on MAINT, please check date/slot and'
               ' aircraft and try again. Thank you.')
    deleted = 'Your Booking has been deleted successfully. Thank you.'
    errors = ('All fields are required, '
              'please check the details and try again. Thank you.')
    sent = ('Your message has been sent, '
            'we will endeavour to reply as soon as we can. Thank you.')
    register = ('Your request to register has been noted.'
                'We will be in touch shortly. Thank you.')
