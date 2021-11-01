from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateNotesDay
from .models import NotesDayFromUser


# Create your views here.


def my_notes_day(request):
    user = request.user.id
    all_comments = NotesDayFromUser.objects.filter(user_id=user).order_by('date_create')



    content = {
        "page_title": 'Првиет!',
        'all_comments': all_comments

    }
    return render(request, 'blogapp/my_notes_day.html', context=content)


def create_note_day(request):

    user = request.user


    if request.method == 'POST':
        print(1)
        # Кароче, не могу схватить пока файлик, посмотри завтра!
        if 'media' in request.FILES:
            form = NotesDayFromUser.objects.create(title=request.POST.get('title'), user_id=user, description=request.POST.get('description'),
                                                    media=request.POST.FILES['media'])
        else:
            form = NotesDayFromUser.objects.create(title=request.POST.get('title'), user_id=user, description=request.POST.get('description'))
        form.save()

        return HttpResponseRedirect(reverse('blog:my_notes_day'))

    else:
        form = CreateNotesDay()
    content = {
        'page_title': 'Создать запись',
        'form': form,
        'user': user
    }

    return render(request, 'blogapp/create_day_note.html', context=content)