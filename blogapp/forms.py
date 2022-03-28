from django import forms
from .models import NotesDayFromUser

class CreateNotesDay(forms.ModelForm):
    class Meta:
        model = NotesDayFromUser
        fields = ['title', 'description', 'media']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите заголовок'
        })
        self.fields['title'].value = ''
        self.fields['title'].label = 'Заголовок для этой записи:'


        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ваши записи'
        })


        self.fields['media'].widget.attrs.update({
            'class': 'form-file'
        })

