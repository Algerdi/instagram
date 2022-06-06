from django.contrib import admin
from tags.models import TaggedItem
from .models import Post
from django.contrib.contenttypes.admin import GenericTabularInline

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
    fields = ['postContent','author', 'image', 'video',]
    list_display =['id', 'postContent','author', 'image',]

    def get_queryset(self, request):
        return super().get_queryset(request).\
            select_related('author').\
            prefetch_related('allComments__author')

class TagInLine(GenericTabularInline):
    model = TaggedItem

class CustomPostAdmin(PostAdmin):
    inlines = [TagInLine]

admin.site.register(Post, CustomPostAdmin)


