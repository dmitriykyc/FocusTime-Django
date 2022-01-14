from wishlistapp.models import WishList


def done_wish(id_wish):
    wish = WishList.objects.get(id=id_wish)
    if wish.is_done:
        wish.is_done = False
    else:
        wish.is_done = True
    wish.save()
