from django.db import models
from posts.models import Post
from instagram import settings

class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=('comment_author'), related_name="comment_author",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='allComments')
    comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, related_name='c_like',  blank=True)
    

    def __str__(self) -> str:
        return f'{self.comment}'


    @property
    def total_likes(self):
        return self.likes.count()