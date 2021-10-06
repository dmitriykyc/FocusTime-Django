from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('registration/', authapp.register, name='registration'),
    path('profile/', authapp.profile, name='profile'),
    path('edit_profile/', authapp.edit_profile, name='edit_form')
]
