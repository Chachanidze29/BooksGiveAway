from django.db import models

from users.models import User


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    condition = models.CharField(max_length=200, default='Good')
    image = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
