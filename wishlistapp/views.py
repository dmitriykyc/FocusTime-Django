from django.http import JsonResponse
from django.shortcuts import render
from wishlistapp.models import WishList
from wishlistapp.services import done_wish


def index(request):
    wish_list = WishList.objects.all()

    content = {
        'wish_list': wish_list,
        'page_title': 'Список целей'
    }

    return render(request, 'wishlistapp/index.html', context=content)


def wish_done(request):
    if request.is_ajax():
        done_wish(request.GET['wish_id'])

        # print()

    return JsonResponse({"name": 'Ok'}, status=200)
