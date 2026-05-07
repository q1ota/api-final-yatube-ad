from django.contrib import admin

from .models import Post, Comment, Group, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'pub_date', 'group')
    search_fields = ('text', 'author__username')
    list_filter = ('pub_date', 'group')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'post', 'created')
    search_fields = ('text', 'author__username')
    list_filter = ('created',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('title', 'slug')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
