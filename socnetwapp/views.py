from django.shortcuts import render


def index(request):
    content = {
        "page_title": 'Hello'
    }
    return render(request, "socnetwapp/index.html", context=content)
