import datetime
from django import forms
from .models import Booking, Contact


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ('username', 'date', 'slot', 'aircraft', 'instructor_requested', 'notes')
        widgets = {
            'date': DateInput(),
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 33, 'placeholder': 'Enter your message here...',}),
            'username': forms.HiddenInput()
        }

    def __init__(self, *args, **kws):
    # To get request.user. Do not use kwargs.pop('user', None) due to potential security hole
        self.username = kws.pop('user')
        super().__init__(*args, **kws)
        self.fields['username'].initial = self.username
        self.fields['username'].disabled = True


class ContactForm(forms.ModelForm):

       class Meta:
        model = Contact
        fields = ('name', 'telephone', 'email', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 33, 'placeholder': 'Enter your message here...',}),
        }

