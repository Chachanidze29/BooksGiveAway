from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework import generics
from users.models import User
from drf_spectacular.utils import extend_schema
from .serializers import BookIdSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['condition', 'author', 'genre']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class Wishlist(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=BookSerializer(many=True),
    )
    def get(self, request):
        user = UserSerializer(request.user)

        return Response({
            'data': user.data['wishlist']
        })

    @extend_schema(
        request=BookIdSerializer
    )
    def post(self, request):
        book_id = request.data.get('book')

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'data': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        if book in user.wishlist.all():
            return Response({'data': 'Book is already in the wishlist.'}, status=status.HTTP_400_BAD_REQUEST)

        user.wishlist.add(book)

        return Response({'data': 'Book added to the wishlist.'}, status=status.HTTP_201_CREATED)


class UsersWithBookInWishlist(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return User.objects.filter(wishlist__id=book_id)

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        recipient = User.objects.get(
            id=request.data.get('recipient_id'))

        if (not recipient.wishlist.filter(id=book_id).exists()):
            return Response({'data': "User doesn't have that book in wishlist"}, status=status.HTTP_404_NOT_FOUND)

        book.recipient = recipient
        book.save()

        return Response({'data': "Success"}, status=status.HTTP_200_OK)
