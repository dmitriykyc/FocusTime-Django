from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserAnswerForm, UserAnswerEditForm
from .models import TasksModel, UserAnswerTasks
from authapp.models import TimeFocusUsers

from .services import get_last_answer_user_and_last_task, checking_for_responce, save_edit_answer, \
    create_answer_for_user


def index(request):
    """Данные для главной страницы со всеми заданиями"""

    page_title = 'План обучения'
    user = request.user

    last_answ_and_task = get_last_answer_user_and_last_task(user=user)

    content = {
        "page_title": page_title,
        "last_answer_user": last_answ_and_task["last_answer_user"],
        "done_tasks": last_answ_and_task["tasks_done"][0:3],
        'tasks_without_answer': last_answ_and_task["tasks_without_answer"]
    }

    return render(request, 'tasksapp/index.html', content)


def tasks_done(request):
    """Показывает пройденные задания"""
    page_title = 'Пройденные задания'
    user = request.user
    tasks_done = get_last_answer_user_and_last_task(user)

    content = {
        'page_title': page_title,
        'done_tasks': tasks_done['tasks_done'],
        'last_answer_user': tasks_done['last_answer_user']
    }

    return render(request, 'tasksapp/tasks_done.html', context=content)


def task(request, pk=None):
    """Отображает страницу с заднием и ответом"""
    content_task = TasksModel.objects.get(id=pk)  # Берём контент с заданием
    page_title = content_task.title
    user = request.user
    progress_bar = get_last_answer_user_and_last_task(user)['tasks_done']  # С права у нас прогресс бар по заданиям

    # Проверяем наличие ответа на это задание
    checking = checking_for_responce(request, pk, user)

    # Если мы получачем ответ на задание:
    if request.POST.get('answer_sent') and pk:
        create_answer_for_user(request, pk, user)
        return HttpResponseRedirect(reverse('tasksapp:task', kwargs={'pk': pk}))

    content = {
        "page_title": page_title,
        'progress_bar': progress_bar,
        'type_form': checking['type_form'],
        'form': checking['form'],
        "content_task": content_task,
        'pk': pk
    }

    return render(request, 'tasksapp/task.html', content)


def edit_answer(request, pk=None):
    """Редактирование уже существующего ответа"""
    page_title = 'Редактор ответа'
    content_task = TasksModel.objects.get(id=pk)
    user = request.user
    answer_if_exist = UserAnswerTasks.objects.get(user_id=user, task_id=pk)

    if request.method == 'POST':
        form = save_edit_answer(request, answer_if_exist, pk)
        return HttpResponseRedirect(reverse('tasksapp:task', kwargs={'pk': pk}))

    else:
        form = UserAnswerEditForm(instance=answer_if_exist)

    content = {
        "page_title": page_title,
        "content_task": content_task,
        'form': form,
        'answer': answer_if_exist

    }

    return render(request, 'tasksapp/update.html', content)


