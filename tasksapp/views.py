from django.shortcuts import render, redirect

from .forms import UserAnswerForm, UserEditForm
from .models import TasksModel, UserAnswerTasks
from authapp.models import TimeFocusUsers


def index(request):
    page_title = 'План обучения'
    user = request.user
    if UserAnswerTasks.objects.filter(user_id=user).order_by('-task_id'):
        last_task = UserAnswerTasks.objects.filter(user_id=user).order_by('-task_id')[0]
    else:
        last_task = None
    tasks = TasksModel.objects.filter(is_activ=1)

    content = {
        "page_title": page_title,
        "last_task": last_task,
        "tasks": tasks
    }

    return render(request, 'tasksapp/index.html', content)


# Попасть сюда можно впринципе только зареганным пользователям, user_id просто там ниже обязательно у меня стоит
def task(request, pk=None):
    page_title = 'Задания'
    content_task = TasksModel.objects.get(id=pk)
    all_task = TasksModel.objects.all()

    user = TimeFocusUsers.objects.get(id=request.user.id)

    if UserAnswerTasks.objects.filter(user_id=request.user.id, task_id=pk):  # Если у БД уже есть ответ на это задание
        type_form = 1  # Сделаем так для того чтобы определить что сейчас выводить
        answer_if_exist = UserAnswerTasks.objects.get(user_id=request.user.id, task_id=pk)  #Возвращаем этот ответ в форму
        form = answer_if_exist

    else:
        form = UserAnswerForm()
        type_form = 2

    if request.POST.get('answer_sent') and pk:
        answer_text = request.POST.get('answer')
        task_id = TasksModel.objects.get(id=pk)
        if 'media' in request.FILES:
            answer = UserAnswerTasks.objects.create(task_id=task_id, user_id=user, answer=answer_text, media=request.FILES['media'])
        else:
            answer = UserAnswerTasks.objects.create(task_id=task_id, user_id=user, answer=answer_text)
        answer.save()
        return redirect('tasksapp:task', pk=pk)

    content = {
        "page_title": page_title,
        "content_task": content_task,
        'all_task': all_task,
        'form': form,
        'type_form': type_form,
        'pk': pk
    }

    return render(request, 'tasksapp/task.html', content)


def edit_answer(request, pk=None):
    page_title = 'Редактировать ответ'
    content_task = TasksModel.objects.get(id=1)
    user = TimeFocusUsers.objects.get(id=request.user.id)
    answer_if_exist = UserAnswerTasks.objects.get(user_id=request.user.id, task_id=pk)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=answer_if_exist)
        if form.is_valid():
            answer_if_exist.answer = request.POST['answer']
            answer_if_exist.user_id = user
            answer_if_exist.media = request.FILES['media']
            answer_if_exist.save()
            return redirect('tasksapp:task', pk)

    else:
        form = UserEditForm(instance=answer_if_exist)

    content = {
        "page_title": page_title,
        "content_task": content_task,
        'form': form
    }

    return render(request, 'tasksapp/update.html', content)
