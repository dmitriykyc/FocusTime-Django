from django.urls import path
import socnetwapp.views as socnetwapp

app_name = 'socnetwapp'

urlpatterns = [
    path('', socnetwapp.index, name='socnetwapp'),
    path('create_post', socnetwapp.create_post, name='create_post'),
    path('my_posts', socnetwapp.my_posts, name='my_posts'),
    path('edit_post/<int:pk>', socnetwapp.edit_post, name='edit_post'),
    path('delete_post/<int:pk>', socnetwapp.delete_post, name='delete_post'),
]
