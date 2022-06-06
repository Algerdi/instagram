from django.contrib import admin
from . import models

@admin.register(models.TaggedItem)
class TagAdmin(admin.ModelAdmin):
    list_display =  ['tag','object_id','content_object', 'content_type' ]