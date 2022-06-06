from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'author','post', 'comment', 'time']

admin.site.register(Comment, CommentAdmin)
