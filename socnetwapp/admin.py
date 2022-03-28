from django.contrib import admin

from socnetwapp.models import GroupPosts, PostToTheFeed, CommentToThePost

admin.site.register(GroupPosts)
admin.site.register(PostToTheFeed)
admin.site.register(CommentToThePost)
