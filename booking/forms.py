import datetime
from django import forms
from .models import Booking, Contact, Group_Member
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, EmailValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ('username', 'date', 'slot', 'aircraft', 'instructor_requested', 'notes')
        widgets = {
            # 'date': DateInput(),
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 33, 'placeholder': 'Enter your message here...',}),
            'username': forms.HiddenInput(),
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
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 33, 'placeholder': 'Enter your message here...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'maverick@topgun.com'}),
            'telephone': forms.TextInput(attrs={'placeholder': '+44 1234567890', 'rows': 1, 'cols': 33})
        }
