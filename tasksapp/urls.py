from django.urls import path
import tasksapp.views as tasksapp

app_name = 'tasksapp'

urlpatterns = [
    path('', tasksapp.index, name='index'),

]
