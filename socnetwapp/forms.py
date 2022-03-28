from django import forms

from socnetwapp.models import CommentToThePost, PostToTheFeed


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


class CreateNewPost(forms.ModelForm):
    class Meta:
        model = PostToTheFeed
        fields = ['title', 'description', 'media', 'group_posts_id']

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
