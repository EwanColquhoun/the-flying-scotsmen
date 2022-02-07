from django import forms
from .models import Booking, Contact


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('username', 'date', 'slot', 'aircraft',
                  'instructor_requested', 'notes')
        widgets = {
            'notes': forms.Textarea(
                attrs={'rows': 4, 'cols': 33,
                       'placeholder': 'Enter your message here...', }),
            'username': forms.HiddenInput(),
        }

    def __init__(self, *args, **kws):
        """
        Initialises the Booking form with the username of the logged in User.
        Then disables the username field to prevent booking under
        another username.
        """
        # To get request.user.
        # Do not use kwargs.pop('user', None) due to potential security hole
        self.username = kws.pop('user')
        super().__init__(*args, **kws)
        self.fields['username'].initial = self.username
        self.fields['username'].disabled = True


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'telephone', 'email', 'message')
        widgets = {
            'message': forms.Textarea(
                attrs={'rows': 4, 'cols': 33,
                       'placeholder': 'Enter your message here...'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'maverick@topgun.com'}),
            'telephone': forms.TextInput(
                attrs={'placeholder': '+44 1234567890',
                       'rows': 1, 'cols': 33})
        }
