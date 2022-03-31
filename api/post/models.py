from django.db import models
from django.urls import reverse


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})
