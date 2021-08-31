from django.shortcuts import render, redirect

from .forms import UserAnswerForm, UserEditForm
from .models import TasksModel, UserAnswerTasks
from authapp.models import TimeFocusUsers


# Create your views here.

# Попасть сюда можно впринципе только зареганным пользователям, user_id просто там ниже обязательно у меня стоит
def index(request, pk=None):
    page_title = 'Задания'
    content_task = TasksModel.objects.get(id=pk)

    user = TimeFocusUsers.objects.get(id=request.user.id)


    # print(UserAnswerTasks.objects.filter(user_id=request.user.id))

    if UserAnswerTasks.objects.filter(user_id=request.user.id, task_id=pk):
        type_form = 1  # Сделаем так для того чтобы определить что сейчас выводить
        answer_if_exist = UserAnswerTasks.objects.get(user_id=request.user.id, task_id=pk)
        form = answer_if_exist

    else:
        form = UserAnswerForm()
        type_form = 2

    if request.POST.get('answer_sent') and pk:
        answer_text = request.POST.get('answer')
        task_id = TasksModel.objects.get(id=pk)
        answer = UserAnswerTasks.objects.create(task_id=task_id, user_id=user, answer=answer_text)
        answer.save()
        return redirect('tasksapp:index_tasks', pk=pk)

        #Ту ту нас создаётся постоянно новый объект, нужно сделать так:
        # Когда задание уже пройдено, нет формы для ответа, есть только кнопка изменить. И там меняем просто:
        # aaa = UserAnswerTasks.objects.get(id)
        # aaa.answer = 'NEW TEXT'
        # aaa.save()


    content = {
        "page_title": page_title,
        "content_task": content_task,
        'form': form,
        'type_form': type_form,
        'pk': pk
    }

    return render(request, 'tasksapp/index.html', content)


def edit_answer(request, pk=None):
    page_title = 'Редактировать ответ'
    content_task = TasksModel.objects.get(id=1)
    user = TimeFocusUsers.objects.get(id=request.user.id)
    answer_if_exist = UserAnswerTasks.objects.get(user_id=request.user.id, task_id=pk)



    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=answer_if_exist)
        if form.is_valid():
            answer_if_exist.answer = request.POST['answer']
            answer_if_exist.user_id = user
            answer_if_exist.save()
            return redirect('tasksapp:index_tasks', pk)

    else:
        form = UserEditForm(instance=answer_if_exist)

    content = {
        "page_title": page_title,
        "content_task": content_task,
        'form': form
    }

    return render(request, 'tasksapp/update.html', content)