from django.shortcuts import render

from .forms import UserAnswerForm
from .models import TasksModel, UserAnswerTasks


# Create your views here.

def index(request, pk=None):
    page_title = 'Задания'
    content_task = TasksModel.objects.get(id=1)
    form = UserAnswerForm()

    if request.POST.get('answer_sent') and pk:
        answer_text = request.POST.get('answer')
        task_id = TasksModel.objects.get(id=pk)
        answer = UserAnswerTasks.objects.create(task_id=task_id, answer=answer_text)
        answer.save()

        #Ту ту нас создаётся постоянно новый объект, нужно сделать так:
        # Когда задание уже пройдено, нет формы для ответа, есть только кнопка изменить. И там меняем просто:
        # aaa = UserAnswerTasks.objects.get(id)
        # aaa.answer = 'NEW TEXT'
        # aaa.save()


    content = {
        "page_title": page_title,
        "content_task": content_task,
        'form': form
    }

    return render(request, 'tasksapp/index.html', content)