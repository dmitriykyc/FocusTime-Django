from django.contrib.auth.models import User
from django import forms

from tasksapp.models import UserAnswerTasks

class UserAnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}), label=False)

