from django.db import models
from django.conf import settings


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    condition = models.CharField(max_length=200, default='Good')
    image = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='recipient', blank=True, null=True)
