from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import User
from rest_framework import exceptions
from .serializers import UserSerializer
from .authentication import generate_access_token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .authentication import JWTAuthentication


@api_view(["POST"])
def register(request):
    data = request.data
    if (data['password'] != data['password_confirm']):
        raise exceptions.APIException("Passwords don't match")
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({
        'data': serializer.data
    })


@api_view(["POST"])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()

    if (user is None):
        raise exceptions.AuthenticationFailed('Wrong Password')

    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('Wrong Password')

    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def logout(request):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        'message': 'Success'
    }

    return response


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response({
            'data': serializer.data
        })
