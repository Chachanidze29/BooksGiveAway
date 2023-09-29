from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('books.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs', SpectacularSwaggerView.as_view(url_name="schema"))
]
