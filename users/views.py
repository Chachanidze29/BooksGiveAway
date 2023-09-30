from rest_framework.response import Response
from .models import User
from rest_framework import exceptions
from .serializers import UserSerializer
from .authentication import generate_access_token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .authentication import JWTAuthentication


class Register(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        if (data['password'] != data['password_confirm']):
            raise exceptions.APIException("Passwords don't match")
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        })


class Login(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)

        if (user is None):
            raise exceptions.AuthenticationFailed('Wrong Email Address')

        if (not user.check_password(password)):
            raise exceptions.AuthenticationFailed('Wrong Password')

        response = Response()
        token = generate_access_token(user)
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class Logout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'message': 'Success'
        }

        return response


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response({
            'data': serializer.data
        })
