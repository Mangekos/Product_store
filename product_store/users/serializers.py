from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import CustomUser
from .validators import validate_name


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор создания Юзера"""
    username = serializers.CharField(
        max_length=150,
        validators=(validate_name,)
    )
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)

    class Meta:

        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = CustomUser
        fields: tuple = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        )
