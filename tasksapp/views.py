from django.shortcuts import render
from .models import TasksModel

# Create your views here.

def index(request):
    page_title = 'Задания'
    content_task = TasksModel.objects.get(id=1)

    content = {
        "page_title": page_title,
        "content_task": content_task,
    }

    return render(request, 'tasksapp/index.html', content)