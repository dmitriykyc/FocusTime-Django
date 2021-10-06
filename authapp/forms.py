from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms.widgets import HiddenInput
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

class UserEditForm(UserChangeForm):
    class Meta:
        model = TimeFocusUsers
        fields = ('username', 'email', 'avatar', "b_date", "user_info", "instagram", "city")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['username'].help_text = ''
        self.fields['username'].label = 'Ваш логин:'

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите E-mail'
        })


        self.fields['user_info'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['user_info'].help_text = ''
        self.fields['user_info'].label = 'О себе:'

        self.fields['city'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['city'].help_text = ''
        self.fields['city'].label = 'Ваш город:'

        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['avatar'].help_text = ''
        self.fields['avatar'].label = 'Выберите картинку на аватарку:'

        self.fields['instagram'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['instagram'].help_text = ''
        self.fields['instagram'].label = 'Ссылка на инстаграм:'

        self.fields['password'].widget = HiddenInput()
