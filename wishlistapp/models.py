from django.db import models

from authapp.models import TimeFocusUsers


class WishList(models.Model):
    user = models.ForeignKey(TimeFocusUsers, on_delete=models.CASCADE)
    title = models.TextField('Название')
    is_done = models.BooleanField('Выполнена ли цель', default=False)
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата и время изменения', auto_now=True)

    def __str__(self):
        return f'Название: {self.title}'

    class Meta:
        verbose_name = 'Список желаний'
