from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CreateNotesDay
from .models import NotesDayFromUser



def create_new_note_day(request, user):
    if 'media' in request.FILES:
        form = NotesDayFromUser.objects.create(
            title=request.POST.get('title'),
            user_id=user,
            description=request.POST.get('description'),
            media=request.FILES['media'])
    else:
        form = NotesDayFromUser.objects.create(
            title=request.POST.get('title'),
            user_id=user,
            description=request.POST.get('description'))
    form.save()


def edit_note(request, form, note):

    if form.is_valid():
        form.save()
