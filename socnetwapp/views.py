from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from socnetwapp.forms import CreateCommentForm, CreateNewPost
from socnetwapp.models import PostToTheFeed, CommentToThePost, GroupPosts
from socnetwapp.services import create_comment, create_new_post


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


def create_post(request):

    page_title = 'Создать пост'
    user = request.user
    print(1)
    if request.method == 'POST':
        print(1)
        create_new_post(request, user)
        return HttpResponseRedirect(reverse('socnetw:socnetwapp'))

    else:
        form = CreateNewPost()


    content = {
        "page_title": page_title,
        'form': form,
        'user': user
    }

    return  render(request, 'socnetwapp/create-post.html', context=content)