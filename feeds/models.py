from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    content = models.TextField(max_length=1000)
    posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.content[:16]

class Comment(models.Model):
    content = models.TextField(max_length=250)
    posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    relatedPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)