from django.shortcuts import render
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
