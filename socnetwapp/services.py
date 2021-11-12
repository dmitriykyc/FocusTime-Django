from socnetwapp.models import CommentToThePost, PostToTheFeed


def create_comment(request, user):
    """ Сохраняет комментарий в БД """
    comment_text = request.POST.get('text')
    number_post = request.POST.get("id_post")
    to_post = PostToTheFeed.objects.get(id=number_post)

    comment = CommentToThePost.objects.create(from_user_id=user,
                                              text=comment_text,
                                              to_the_post_id=to_post)

    comment.save()