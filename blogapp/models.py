from django.db import models
from authapp.models import TimeFocusUsers

class NotesDayFromUser(models.Model):
    user_id = models.ForeignKey(TimeFocusUsers, verbose_name='id пользователя', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=200, blank=True)
    description = models.TextField('Описание дня')
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата и время изменения', auto_now=True)
    media = models.ImageField('Фото к заданию', blank=True, null=True, upload_to='notes_day_from_user/')
