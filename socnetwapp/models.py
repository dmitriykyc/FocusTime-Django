from django.db import models
from authapp.models import TimeFocusUsers


class GroupPosts(models.Model):
    title = models.CharField('Тематика', max_length=200)
    is_activ = models.BooleanField('Активность группы', default=False)

    def __str__(self):
        return f'{self.title}'


class PostToTheFeed(models.Model):
    id_user = models.ForeignKey(TimeFocusUsers, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=200, blank=True, null=True)
    description = models.TextField('Текст поста')
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата и время изменения', auto_now=True)
    media = models.ImageField('Фото к посту', blank=True, null=True, upload_to='post_to_the_feed/')
    group_posts_id = models.ForeignKey(GroupPosts, verbose_name='Тематика поста', on_delete=models.SET_DEFAULT,
                                       blank=True, null=True, default=None)


class CommentToThePost(models.Model):
    from_user_id = models.ForeignKey(TimeFocusUsers, verbose_name='Коментарий от этого пользователя',
                                     related_name='from_user_id_comment', on_delete=models.CASCADE)
    to_the_post_id = models.ForeignKey(PostToTheFeed, verbose_name='Комментарий к этому посту',
                                       related_name='to_the_post_id_comment', on_delete=models.CASCADE)
    to_the_user_id = models.ForeignKey(TimeFocusUsers, verbose_name='Комментарий для этого пользователя',
                                       related_name='to_the_user_id', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField('Текст комментария')
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата и время изменения', auto_now=True)


class LikesToThePost(models.Model):
    from_user_id = models.ForeignKey(TimeFocusUsers, verbose_name='Лайк от этого пользователя',
                                     on_delete=models.CASCADE)
    post_id = models.ForeignKey(PostToTheFeed, verbose_name='Лайк для этого поста', on_delete=models.CASCADE)
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
