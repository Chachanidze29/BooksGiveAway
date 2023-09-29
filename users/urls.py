from django.urls import path

from .views import register, login, logout
from .views import AuthenticatedUser

urlpatterns = [
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('user', AuthenticatedUser.as_view())
]
