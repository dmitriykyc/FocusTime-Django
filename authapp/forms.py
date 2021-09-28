from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput, ModelForm, Textarea

from authapp.models import TimeFocusUsers

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ваш логин'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })




class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'email')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Придумайте логин для входа '
        })
        self.fields['username'].help_text = ''
        self.fields['username'].label = 'Ваш логин'

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите E-mail'
        })

        self.fields['password1'].help_text = ''
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Придумайте пароль'
        })

        self.fields['password2'].help_text = ''
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Повторите пароль'
        })

