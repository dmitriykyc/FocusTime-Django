from django.urls import path
import socnetwapp.views as socnetwapp

app_name = 'socnetwapp'

urlpatterns = [
    path('', socnetwapp.index, name='socnetwapp'),
    path('create_post', socnetwapp.create_post, name='create_post')
]
