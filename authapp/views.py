from django.shortcuts import render, redirect
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegistrationForm, UserEditForm
from django.contrib import auth
from django.http import HttpResponseRedirect

from authapp.models import TimeFocusUsers


def register(request):
    page_title = 'Регистрация'
    form = UserRegistrationForm()

    if request.POST.get('registration'):
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/index.html')

    content = {
        'form': form,
        'page_title': page_title
    }

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
            return redirect('index')

    content = {
        'form': form,
        "page_title": page_title
    }

    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return redirect('index')


def profile(request):
    page_title = "Ваш профиль"
    user = TimeFocusUsers.objects.get(id=request.user.id)

    content = {
        "page_title": page_title,
        "user": user
    }

    return render(request, 'authapp/profile.html', content)

def edit_profile(request):
    page_title = 'Редактирование профиля'
    this_instance = TimeFocusUsers.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=this_instance)
        if form.is_valid():
            form.save()
            # return render(request, 'authapp/profile.html')
            return HttpResponseRedirect(reverse('authapp:profile'))
    else:
        form = UserEditForm(instance=this_instance)

    content = {
        'form': form,
        'page_title': page_title
    }

    return render(request, 'authapp/edit_profile.html', context=content)