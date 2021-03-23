from django.db import models
from django.contrib.auth.models import User


class News(models.Model):

    title = models.CharField(max_length=80)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
