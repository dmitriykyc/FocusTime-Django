from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from socnetwapp.forms import CreateCommentForm, CreateNewPost
from socnetwapp.models import PostToTheFeed, CommentToThePost, GroupPosts
from socnetwapp.services import create_comment, create_new_post, del_post


def index(request):

    user = request.user
    posts = PostToTheFeed.objects.all().order_by("-date_create")
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
    if request.method == 'POST':
        create_new_post(request, user)
        return HttpResponseRedirect(reverse('socnetw:socnetwapp'))

    else:
        form = CreateNewPost(initial={'group_posts_id': 1})


    content = {
        "page_title": page_title,
        'form': form,
        'user': user
    }

    return render(request, 'socnetwapp/create-post.html', context=content)


def my_posts(request):

    user = request.user
    posts = PostToTheFeed.objects.filter(id_user=user).order_by("-date_create")

    content = {
        "page_title": 'Мои посты',
        "posts": posts
    }

    return render(request, 'socnetwapp/my_posts.html', context=content)


def edit_post(request, pk):
    page_title = 'Редактирование поста'
    user = request.user
    content_post = PostToTheFeed.objects.get(id=pk)

    if request.method == 'POST':
        create_new_post(request, user)
        return HttpResponseRedirect(reverse('socnetw:my_posts'))

    else:
        form = CreateNewPost(instance=content_post)

    content = {
        "page_title": page_title,
        'form': form,
        'user': user
    }

    return render(request, 'socnetwapp/edit_post.html', context=content)


def delete_post(request, pk):
    del_post(pk)
    return HttpResponseRedirect(reverse('socnetwapp:socnetwapp'))