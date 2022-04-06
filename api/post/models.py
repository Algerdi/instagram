from django.db import models
from django.urls import reverse
from user.models import NewUser

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(NewUser, related_name="posts", on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})
