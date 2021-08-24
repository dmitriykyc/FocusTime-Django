from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import TimeFocusUsers

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'password')



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'b_date', 'user_info', "instagram", 'city')

