from django.urls import path

from .views import Register, Login, Logout
from .views import AuthenticatedUser

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view()),
    path('user', AuthenticatedUser.as_view())
]
