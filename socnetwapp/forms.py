from django import forms

from socnetwapp.models import CommentToThePost


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = CommentToThePost
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-control form-control-flush',
            'placeholder': 'Введите комментарий',
            'rows': '1'
        })