from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext as _

from .models import *


class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        username = self.fields['username']
        password = self.fields['password']

        username.label = _("Foydalanuvchi nomi")
        password.label = _("Parol")

        username.widget.attrs.update({'class': "form-control"})
        password.widget.attrs.update({'class': "form-control"})


class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email']

        labels = {
            'username': _("Foydalanuvchi nomi"),
            'email': _("Elektron pochta manzili")
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        username = self.fields['username']
        email = self.fields['email']
        password1 = self.fields['password1']
        password2 = self.fields['password2']

        username.widget.attrs.update({'class': "form-control"})
        email.widget.attrs.update({'class': "form-control"})
        password1.widget.attrs.update({'class': "form-control"})
        password2.widget.attrs.update({'class': "form-control"})
