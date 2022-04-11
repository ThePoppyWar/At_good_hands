from django import forms
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

