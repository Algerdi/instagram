from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['created']

