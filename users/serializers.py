from rest_framework import serializers
from .models import User
from books.serializers import BookSerializer


class UserSerializer(serializers.ModelSerializer):
    wishlist = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'password', 'date_joined', 'wishlist']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if (password is not None):
            instance.set_password(password)

        instance.save()

        return instance
