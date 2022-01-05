from django.shortcuts import render
from commentapp.models import Comments

def index(request):

    user = request.user
    comments = Comments.objects.all()

    content = {
        "page_title": 'Новостная лента',
        "comments": comments,
    }
    return render(request, "commentapp/index.html", context=content)
