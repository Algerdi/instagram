from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class TaggedItemManager(models.Manager):
    """
    Usefull functions
    """
    def get_tags_for(self, obj_type, obj_id):
        """"
        Finds all tags for a given post
        """
        content_type = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects. \
            filter(
                content_type=content_type, 
                object_id = obj_id)

    def create_tags(self, obj_type, obj_id, tag):
        """
        Creates a new tag
        """
        content_type = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects. \
                create(
                    content_type=content_type, 
                    object_id = obj_id, 
                    tag = tag)

    def get_all_identical_tags(self, obj_type, tag):
        """
        Returns list with all identical tags_label
        """
        content_type = ContentType.objects.get_for_model(obj_type)
        return TaggedItem.objects. \
                filter(
                    content_type=content_type,
                    tag = tag)

    def get_all_unique_tags(self, obj_type):
        """"
        Returns list with all unique tags_label
        """
        content_type = ContentType.objects.get_for_model(obj_type)
        tagged_objects = TaggedItem.objects. \
                filter(
                    content_type=content_type)
        tags_list_label = []
        for tag in tagged_objects:
            if tag.tag not in tags_list_label:
                tags_list_label.append(tag.tag)
        return tags_list_label

    def get_id_list(self,  obj_type, tag ):
        """"
        Returns id list which includes id of all posts, where the given tag is applied to
        """
        content_type = ContentType.objects.get_for_model(obj_type)
        tagged_objects = TaggedItem.objects. \
                filter(
                    content_type=content_type,
                    tag = tag)
        id_list = []
        for tag in tagged_objects:
            id_list.append(tag.object_id)
        return id_list


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id' )
    def __str__(self) -> str:
        return self.tag
