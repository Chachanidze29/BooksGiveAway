from rest_framework import serializers
from .models import Book
from .models import User
from rest_framework import exceptions


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author',
                  'genre', 'location', 'condition', 'image', 'owner_id']
