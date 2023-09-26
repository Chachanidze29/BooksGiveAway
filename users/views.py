from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework import exceptions
from .serializers import UserSerializer


@api_view(["POST"])
def register(request):
    data = request.data
    if (data['password'] != data['password_confirm']):
        raise exceptions.APIException("Passwords don't match")
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def users(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)
