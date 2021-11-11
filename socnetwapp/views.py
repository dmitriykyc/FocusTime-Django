from django.shortcuts import render
from socnetwapp.models import PostToTheFeed

def index(request):

    posts = PostToTheFeed.objects.all()

    content = {
        "page_title": 'Новостная лента',
        "posts": posts
    }
    return render(request, "socnetwapp/index.html", context=content)
