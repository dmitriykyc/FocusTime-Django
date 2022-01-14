from django import forms
from .models import WishList

class CreateWish(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ['title']



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Сформулируйте желание',
            'rows': 3
        })
        self.fields['title'].value = ''
        self.fields['title'].label = 'Заголовок для этой записи:'



    #     self.fields['description'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Ваши записи'
    #     })
    #
    #
    #     self.fields['media'].widget.attrs.update({
    #         'class': 'form-file'
    #     })

