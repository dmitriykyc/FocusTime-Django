from socnetwapp.models import CommentToThePost, PostToTheFeed, GroupPosts


def create_comment(request, user):
    """ Сохраняет комментарий в БД """
    comment_text = request.POST.get('text')
    number_post = request.POST.get("id_post")
    to_post = PostToTheFeed.objects.get(id=number_post)

    comment = CommentToThePost.objects.create(from_user_id=user,
                                              text=comment_text,
                                              to_the_post_id=to_post)

    comment.save()


def create_new_post(request, user):
    if not request.POST.get('group_posts_id'):
        group_posts_id = GroupPosts.objects.get(id=5)
    else:
        group_posts_id = GroupPosts.objects.get(id=request.POST.get('group_posts_id'))

    if 'media' in request.FILES:
        form = PostToTheFeed.objects.create(
            title=request.POST.get('title'),
            id_user=user,
            description=request.POST.get('description'),
            media=request.FILES['media'],
            group_posts_id=group_posts_id)
    else:
        form = PostToTheFeed.objects.create(
            title=request.POST.get('title'),
            id_user=user,
            description=request.POST.get('description'),
            group_posts_id=group_posts_id)
    form.save()


def del_post(pk):
    post_to_delete = PostToTheFeed.objects.get(id=pk)
    post_to_delete.delete()