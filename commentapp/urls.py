from django.urls import path
import commentapp.views as commentapp

app_name = 'comment'

urlpatterns = [
    path('1/', commentapp.index, name='index')
]
