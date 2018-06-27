from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=1024)
    is_published = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User, models.PROTECT)


class Comment(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=240)
    date_created = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    post = models.ForeignKey(Post, models.CASCADE)

    def __str__(self):
        return self.text