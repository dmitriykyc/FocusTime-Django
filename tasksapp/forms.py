from django.contrib.auth.models import User
from django import forms

from tasksapp.models import UserAnswerTasks

class UserAnswerForm(forms.ModelForm):
    # answer = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}), label=False)
    # is_public = forms.BooleanField(label='Сделать ответ публичным')
    # image = forms.ImageField(widget=forms.ImageField(attrs={"enctype":"multipart/form-data"}))
    #
    class Meta:
        model = UserAnswerTasks
        fields = ['answer', 'is_public', 'media']



class UserEditForm(forms.ModelForm):

    class Meta:
        model = UserAnswerTasks
        fields = ['answer', 'is_public', 'media']





