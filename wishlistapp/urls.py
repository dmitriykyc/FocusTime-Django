from django.urls import path
import socnetwapp.views as socnetwapp

app_name = 'wishlistapp'

urlpatterns = [
    path('', wishlistapp.index, name='index')
]
