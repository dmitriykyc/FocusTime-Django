from django.contrib.auth.models import User
from django import forms
from tasksapp.models import UserAnswerTasks
from django.forms import Textarea


class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswerTasks
        fields = ['answer', 'is_public', 'media']




class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserAnswerTasks
        fields = ['answer', 'is_public', 'media']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['media'].widget.attrs.update({'class': 'form-control'})

