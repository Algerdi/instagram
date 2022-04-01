from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Post(models.Model):
    postContent = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f'{self.postContent}'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='allComments')
    comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.comment}'
