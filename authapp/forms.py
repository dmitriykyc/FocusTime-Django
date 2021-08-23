from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from authapp.models import TimeFocusUsers

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'password')

