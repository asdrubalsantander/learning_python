from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    created_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
