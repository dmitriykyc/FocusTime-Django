from wishlistapp.models import WishList
from django.http import JsonResponse


def done_wish(id_wish):
    wish = WishList.objects.get(id=id_wish)
    if wish.is_done:
        wish.is_done = False
    else:
        wish.is_done = True
    wish.save()


def add_wish_bd(user, request):
    title = request.POST.get('title')
    new_wish = WishList.objects.create(title=title, user=user)
    new_wish.save()


def delete_wish(wish_id):
    wish_to_del = WishList.objects.get(id=int(wish_id))
    wish_to_del.delete()

