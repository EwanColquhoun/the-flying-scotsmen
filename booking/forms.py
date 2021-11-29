import datetime
from django import forms
from .models import Booking, Contact, Group_Member
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, EmailValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    username = forms.CharField(max_length=30, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=False, help_text='Required. Input a valid email address.')


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = Group_Member
        fields = ('message',)
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 33, 'placeholder': 'Enter your message here...'}),
        }
    
    def clean_message(self):

        message = self.cleaned_data['message']

        if len(message)<6:
            msg = 'username is too short'
            self.add_error('message', msg)

        return message