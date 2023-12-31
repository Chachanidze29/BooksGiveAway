from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Book


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    wishlist = models.ManyToManyField(
        Book, blank=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
