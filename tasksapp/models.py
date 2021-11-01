from django.db import models
from tinymce.models import HTMLField
from authapp.models import TimeFocusUsers
# Create your models here.

class TasksModel(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    serial_numb_task = models.IntegerField('Порядковый номер задания')
    logo = models.ImageField('Лого задания', blank=True, null=True, upload_to='logo_task/')
    description = models.TextField('Описание')
    is_activ = models.BooleanField('Активность задания', default=True)
    date_create = models.DateField('Дата создания', auto_now_add=True)
    date_update = models.DateField('Дата изменения', auto_now=True)
    content = HTMLField()

    def __str__(self):
        return f'Заголовок: ({self.title})'


class NoteAnswer(models.Model):
    pass


class UserAnswerTasks(models.Model):
    task_id = models.ForeignKey(TasksModel, verbose_name='id задания', on_delete=models.CASCADE)
    user_id = models.ForeignKey(TimeFocusUsers, verbose_name='id пользователя', on_delete=models.CASCADE)
    is_public = models.BooleanField('Сделать публичным?', default=True)
    answer = models.TextField('Ответ на задание')
    media = models.ImageField('Фото к заданию', blank=True, null=True, upload_to='answer/')
    date_create = models.DateField('Дата создания', auto_now_add=True)
    date_update = models.DateField('Дата изменения', auto_now=True)

    def __str__(self):
        return f'task_id ({self.task_id}), user_id ({self.user_id})'

