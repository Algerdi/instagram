from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class User(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    postContent = models.CharField(max_length=500)


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='allComments')
    comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)


# class LikedComment(models.Model):
#     commentLiked = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()
