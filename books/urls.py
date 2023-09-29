from rest_framework import routers
from django.urls import path, include
from books.views import BookViewSet, Wishlist, UsersWithBookInWishlistView

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/wishlist', Wishlist.as_view()),
    path('books/<int:book_id>/users/',
         UsersWithBookInWishlistView.as_view()),
]
