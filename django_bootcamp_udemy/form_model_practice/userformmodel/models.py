from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=120)
