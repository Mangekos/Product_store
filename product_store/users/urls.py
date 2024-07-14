from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewset

router = DefaultRouter()

router.register('users', CustomUserViewset)

urlpatterns: list = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]
