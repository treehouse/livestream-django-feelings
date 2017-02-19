from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LogoutForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
