from django.urls import path
import socnetwapp.views as socnetwapp

app_name = 'socnetwapp'

urlpatterns = [
    path('', socnetwapp.index, name='socnetwapp'),
]
