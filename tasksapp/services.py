from django.shortcuts import redirect

from .forms import UserAnswerForm, UserAnswerEditForm
from .models import UserAnswerTasks, TasksModel


def get_last_answer_user_and_last_task(user):
    '''Получает задание, на которое пользователь дал последний ответ'''

    # Берём ответ на последнее задание у этого пользователя
    tasks_without_answer = []
    tasks_done = []

    # Весь список заданий
    all_tasks = TasksModel.objects.filter(is_activ=1).order_by("serial_numb_task")

    if UserAnswerTasks.objects.filter(user_id=user):
        last_answer_user = UserAnswerTasks.objects.filter(user_id=user).order_by('-task_id')[0]
        # Берём последнее задание пройденное у этого пользователя
        last_task_done = TasksModel.objects.get(id=last_answer_user.task_id.id)

        for task in all_tasks:
            if task.serial_numb_task <= last_task_done.serial_numb_task:
                tasks_done.append(task)
            else:
                tasks_without_answer.append(task)
    else:
        last_answer_user = None
        tasks_without_answer = all_tasks


    return {"last_answer_user": last_answer_user,
            "tasks_without_answer": tasks_without_answer,
            "tasks_done": tasks_done}


def checking_for_responce(request, pk: int, user):
    """Проверяет наличие ответа на вопрос и отправляет форму и тип формы (для ответа или уже с ответом)"""
    if UserAnswerTasks.objects.filter(user_id=request.user.id, task_id=pk):  # Если у БД уже есть ответ на это задание
        type_form = 1  # Тип для показа уже существующего ответа
        answer_if_exist = UserAnswerTasks.objects.get(user_id=request.user.id,
                                                      task_id=pk)  # Возвращаем этот ответ в форму
        form = answer_if_exist

    else:
        form = UserAnswerForm()
        type_form = 2 # Форма пустая для заполнения

    return {
        'type_form': type_form,
        'form': form,
    }


def save_edit_answer(request, answer_if_exist, pk):
    """Редактирование уже существующего ответа"""
    form = UserAnswerEditForm(request.POST, request.FILES, instance=answer_if_exist)
    if form.is_valid():
        form.save()

    return form








def create_answer_for_user(request, pk, user):
    """Сохраняет ответ в БД"""
    answer_text = request.POST.get('answer')
    task_id = TasksModel.objects.get(id=pk)
    if 'mediaq' in request.FILES:
        answer = UserAnswerTasks.objects.create(task_id=task_id, user_id=user, answer=answer_text,
                                                media=request.FILES['media'])
    else:
        answer = UserAnswerTasks.objects.create(task_id=task_id, user_id=user, answer=answer_text)
    answer.save()
