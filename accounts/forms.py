from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from booking.models import Group_Member
from .models import CustomUser


class CustomSignUpForm(UserCreationForm, SignupForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 33, 'placeholder': 'Why do you want to join The Flying Scotsmen...'}),
        }

    username = forms.CharField(max_length=30, required=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, label=("Email"), help_text='Required. Input a valid email address.')
    # password1 = forms.PasswordField(
    #         label=_("Password"), autocomplete="new-password")
    # password2 = forms.PasswordField(label=_("Password (again)"))
    message = forms.Textarea()


    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.message = self.cleaned_data['message']
        user.save()
        return user


# class UserMessageForm(forms.ModelForm):
#     class Meta:
#         model = Group_Member
#         fields = ('message',)
#         widgets = {
#             'message': forms.Textarea(attrs={'rows': 4, 'cols': 33, 'placeholder': 'Why you want to join The Flying Scotsmen...'}),
#         }
    
#     def clean_message(self):

#         message = self.cleaned_data['message']

#         if len(message) < 6:
#             msg = 'username is too short'
#             self.add_error('message', msg)

#         return message
