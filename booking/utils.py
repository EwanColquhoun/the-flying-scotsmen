from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Booking


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
            if day != 0 and len(events_per_day) == 0:
                return f"<td class='day-free'><a class='btn date' data-bs-toggle='modal' data-bs-target='#myModal' name={self.month}_{day}>{day}</a><ul class='booking_list'> {d} </ul></td>"
            elif day != 0 and len(events_per_day) <= 3:
                return f"<td class='day-medium'><a class='btn date' data-bs-toggle='modal' data-bs-target='#myModal' name={self.month}_{day}>{day}</a><ul class='booking_list'> {d} </ul></td>"
            else:
                return f"<td class='day-full'><a class='btn date' data-bs-toggle='modal' data-bs-target='#myModal' name={self.month}_{day}>{day}</a><ul class='booking_list'> {d} </ul></td>"
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
