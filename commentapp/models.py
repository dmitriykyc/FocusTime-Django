from django.db import models

from authapp.models import TimeFocusUsers
from socnetwapp.models import PostToTheFeed


class Comments(models.Model):
    user = models.ForeignKey(TimeFocusUsers, verbose_name='Коментарий от пользователя', on_delete=models.CASCADE,
                             related_name='user')
    parent_user = models.ForeignKey(TimeFocusUsers, blank=True, null=True,
                                    verbose_name='Кому отвечаем на комент', default=None, on_delete=models.CASCADE,
                                    related_name='parent_user')
    parent_comment = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,
                                       verbose_name='Номер родительского коммента')
    to_post = models.ForeignKey(PostToTheFeed, verbose_name='Комментарий к этому посту',
                                related_name='to_post_comment', on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата и время изменения', auto_now=True)
