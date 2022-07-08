from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from random import random

User = get_user_model()

def pass_length_validation(value):
    if len(value) < 8:
        raise ValidationError("Password too short. Password should be at least 8 characters")


class RegistrationForm(forms.ModelForm):
    pass_1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password"}),
                             validators=[pass_length_validation])
    pass_2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password agine"}),
                             validators=[pass_length_validation])

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'pass_1',
            'pass_2'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }


    def clean(self):
        data = super().clean()
        if data.get('pass_1') != data.get('pass_2'):
            raise ValidationError('Password are not same!')
        return data


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'autofocus': True,'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))



