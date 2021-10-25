from django.urls import path
import tasksapp.views as tasksapp

app_name = 'tasksapp'

urlpatterns = [
    path('', tasksapp.index, name='tasks_index'),
    path('<int:pk>/', tasksapp.task, name='task'),
    path('edit/<int:pk>/', tasksapp.edit_answer, name='edit_answer'),
    path('tasks_done/', tasksapp.tasks_done, name='tasks_done'),

]
