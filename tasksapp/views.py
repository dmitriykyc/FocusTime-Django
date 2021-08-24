from django.shortcuts import render

# Create your views here.

def index(request):
    page_title = 'Задания'

    content = {
        "page_title": page_title
    }

    return render(request, 'tasksapp/index.html', content)