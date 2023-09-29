from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from users.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['condition', 'author', 'genre']


class Wishlist(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserSerializer(request.user)

        return Response({
            'data': user.data['wishlist']
        })

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
