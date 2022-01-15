from django.http import JsonResponse
from django.shortcuts import render
from wishlistapp.models import WishList
from wishlistapp.services import done_wish, add_wish_bd, delete_wish, edit_wish
from .forms import CreateWish


def index(request):
    user = request.user
    wish_list = WishList.objects.filter(user=user)
    form = CreateWish()

    if request.method == 'POST':
        if 'add_wish_bd' in request.POST:
            add_wish_bd(user, request)

    content = {
        'wish_list': wish_list,
        'page_title': 'Список целей',
        'form': form
    }

    return render(request, 'wishlistapp/index.html', context=content)


def wish_done(request):
    if request.is_ajax():
        done_wish(request.GET['wish_id'])

        # print()

    return JsonResponse({"name": 'Ok'}, status=200)


def wish_delete(request):
    if request.is_ajax():
        delete_wish(request.GET['wish_id'])

    return JsonResponse({}, status=200)


def wish_edit(request):
    title = request.POST['text']
    if request.is_ajax():
        if request.method == 'POST' and 'num_form' in request.POST and request.POST['num_form'] == '2':
            edit_wish(request.POST['wish_id'], title)


    return JsonResponse({}, status=200)
