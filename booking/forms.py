import datetime
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ('username', 'date', 'slot', 'aircraft', 'instructor_requested', 'notes')
        widgets = {
            'date': DateInput(),
            'notes': forms.Textarea(attrs={'rows': 5, 'cols': 33, 'placeholder': 'Enter your message here...',}),
        }

    def __init__(self, *args, **kws):
    # To get request.user. Do not use kwargs.pop('user', None) due to potential security hole
        self.username = kws.pop('user')
        super().__init__(*args, **kws)
        self.fields['username'].initial = self.username
        self.fields['username'].disabled = True
