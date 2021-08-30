from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class TasksModel(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    is_activ = models.BooleanField('Активность задания', default=True)
    date_create = models.DateField('Дата создания', auto_now_add=True)
    date_update = models.DateField('Дата изменения', auto_now=True)
    content = HTMLField()

    def __str__(self):
        return self.title