from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def pass_length_validation(value):
    if len(value) < 8:
        raise ValidationError("Password too short. Password should be at least 8 characters")


class RegistrationForm(forms.ModelForm):
    pass_1 = forms.CharField(widget=forms.PasswordInput(), validators=[pass_length_validation])
    pass_2 = forms.CharField(widget=forms.PasswordInput(), validators=[pass_length_validation])

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'pass_1',
            'pass_2'
        ]

    def clean(self):
        data = super().clean()
        if data.get('pass_1') != data.get('pass_2'):
            raise ValidationError('Password are not same!')
        return data


class LoginForm(forms.Form):
    username = None
    email = UsernameField(widget=forms.EmailInput(
        attrs={'autofocus': True, 'placeholder': "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}))

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'email': self.username_field.verbose_name},
        )

    error_messages = {
        'invalid_login': (
            "Please enter a valid email address and password"
        ),
        'inactive': ("Account is inactive.")
    }
