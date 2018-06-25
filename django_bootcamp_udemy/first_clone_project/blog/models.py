from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1024)
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)


class Comment(models.Model):
    username = models.CharField(max_length=120)
    text = models.CharField(max_length=140)
    date_created = models.DateField(auto_now_add=True)
    is_aproved = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
