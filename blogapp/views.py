from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateNotesDay
from .models import NotesDayFromUser

# Create your views here.
from .services import create_new_note_day, edit_note


def my_notes_day(request):
    """Показывает все записи о прошедших днях от пользователя"""
    user = request.user.id
    all_comments = NotesDayFromUser.objects.filter(user_id=user).order_by('-date_create')

    content = {
        "page_title": 'Првиет!',
        'all_comments': all_comments

    }
    return render(request, 'blogapp/my_notes_day.html', context=content)


def create_note_day(request):
    """Создаёт новую запись о прошедшем дне"""
    user = request.user

    if request.method == 'POST':
        create_new_note_day(request, user)
        return HttpResponseRedirect(reverse('blog:my_notes_day'))

    else:
        form = CreateNotesDay()

    content = {
        'page_title': 'Создать запись',
        'form': form,
        'user': user
    }

    return render(request, 'blogapp/create_day_note.html', context=content)


def edit_note_day(request, pk):
    """Редактирование заметки дня"""
    note = NotesDayFromUser.objects.get(id=pk)

    if request.method == 'POST':
        form = CreateNotesDay(request.POST, request.FILES, instance=note)
        edit_note(request, form, note)
        return HttpResponseRedirect(reverse('blog:my_notes_day'))

    else:
        form = CreateNotesDay(instance=note)

    content = {
        "page_title": "Редактирование",
        "note": note,
        "form": form
    }
    return render(request, 'blogapp/edit_note_day.html', content)


def delete_note_day(request, pk):
    """Удаляет свою запись"""
    note = NotesDayFromUser.objects.get(id=pk)
    note.delete()
    return HttpResponseRedirect(reverse('blog:my_notes_day'))
