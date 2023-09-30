from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author',
                  'genre', 'location', 'condition', 'image', 'owner', 'recipient']


class BookIdSerializer(serializers.Serializer):
    book = serializers.IntegerField()
