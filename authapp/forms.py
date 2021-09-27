from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import TimeFocusUsers

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control'
            field.help_text = ''
            print(field_name)
            print("*" * 20)
            print(field)