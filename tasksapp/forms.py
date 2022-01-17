from django.contrib.auth.models import User
from django import forms
from tasksapp.models import UserAnswerTasks
from django.forms import Textarea


class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswerTasks
        fields = ['answer', 'is_public', 'media']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs.update({
            'data-quill': '{"placeholder": "Quill WYSIWYG"}'
        })
        self.fields['is_public'].widget.attrs.update({
            'class': 'form-check-input'
        })
        self.fields['media'].widget.attrs.update({
            'class': 'form-file'
        })




class UserAnswerEditForm(forms.ModelForm):
    class Meta:
        model = UserAnswerTasks
        fields = ['answer', 'is_public', 'media']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ваши записи'
        }),
        self.fields['is_public'].widget.attrs.update({
            'class': 'form-check-input'
        })