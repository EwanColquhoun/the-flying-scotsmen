from .models import Booking
from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('username', 'date', 'slot', 'aircraft', 'instructor_requested', 'notes')
        widgets = {
            'date': DateInput()
        }
