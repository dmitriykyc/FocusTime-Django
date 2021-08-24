from django.shortcuts import render
from authapp.forms import UserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect


def register(request):
    page_title = 'Регистрация'
    content = {'page_title': page_title}

    return render(request, 'authapp/registration.html', context=content)


def login(request):
    page_title = 'Вход в систему'
    form = UserLoginForm()
    if request.POST.get('login'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            print(1)
            return render(request, 'mainapp/index.html')

    content = {
        'form': form,
        "page_title": page_title
    }

    return render(request, 'authapp/login.html', content)


def logout(request):
    print(1)
    auth.logout(request)
    return render(request, 'mainapp/index.html')
