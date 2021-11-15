from django.shortcuts import render

from socnetwapp.forms import CreateCommentForm
from socnetwapp.models import PostToTheFeed, CommentToThePost, GroupPosts
from socnetwapp.services import create_comment


def index(request):

    user = request.user
    posts = PostToTheFeed.objects.all()
    category_post = GroupPosts.objects.filter(is_activ=True)
    form = CreateCommentForm()

    if request.method == 'POST':
        create_comment(request, user)

    content = {
        "page_title": 'Новостная лента',
        "posts": posts,
        "form": form,
        "category_post": category_post
    }
    return render(request, "socnetwapp/index.html", context=content)
