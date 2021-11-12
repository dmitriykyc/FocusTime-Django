from django.shortcuts import render

from socnetwapp.forms import CreateCommentForm
from socnetwapp.models import PostToTheFeed, CommentToThePost
from socnetwapp.services import create_comment

def index(request):

    user = request.user
    posts = PostToTheFeed.objects.all()
    form = CreateCommentForm()

    if request.method == 'POST':
        create_comment(request, user)

    content = {
        "page_title": 'Новостная лента',
        "posts": posts,
        "form": form
    }
    return render(request, "socnetwapp/index.html", context=content)
