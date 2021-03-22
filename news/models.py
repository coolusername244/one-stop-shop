from django.db import models


class News(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    # image
    date = models.DateTimeField(auto_now_add=True)
    # author
