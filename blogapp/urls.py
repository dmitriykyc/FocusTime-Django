from django.urls import path
import blogapp.views as blogapp

app_name = 'blogapp'

urlpatterns = [
    path('my_notes_day/', blogapp.my_notes_day, name='my_notes_day'),
    path('create_note_day/', blogapp.create_note_day, name='create_note_day'),
    path('edit/<int:pk>/', blogapp.edit_note_day, name='edit_note_day'),
    path('delete/<int:pk>/', blogapp.delete_note_day, name='delete_note_day'),
]
