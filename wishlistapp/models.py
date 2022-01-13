from django.db import models


class WishList(models.Model):
    title = models.TextField('Название')
    is_done = models.BooleanField('Выполнена ли цель', default=False)
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата и время изменения', auto_now=True)

    def __str__(self):
        return f'Название: {self.title}'
