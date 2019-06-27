""" Post Admin Classes"""

# Django
from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    list_display = ('pk', 'title', 'photo', 'created', 'modified', 'user_id')
    list_display_links = ('pk', 'user_id')
    list_editable = ('photo', 'title')
    search_fields = ('user_id', 'title', 'user__username')
    list_filter = ('created', 'modified')
