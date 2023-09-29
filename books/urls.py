from rest_framework import routers
from django.urls import path, include
from books.views import BookViewSet, Wishlist

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/wishlist', Wishlist.as_view())
]
