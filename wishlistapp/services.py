from wishlistapp.models import WishList


def done_wish(id_wish):
    wish = WishList.objects.get(id=id_wish)
    wish.is_done = True
    wish.save()
