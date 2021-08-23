from django.shortcuts import render
from authapp.forms import UserLoginForm
from django.contrib import auth


def register(request):
    page_title = 'Регистрация'

    content = {'page_title': page_title}

    return render(request, 'authapp/registration.html', context=content)

def login(request):
    page_title = 'Вход в систему'
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            print(1)
            print(request)

    else:
        form = UserLoginForm()
    content = {
        'form': form,
        "page_title": page_title
    }

    return render(request, 'authapp/login.html', content)