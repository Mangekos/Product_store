from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_name


class CustomUser(AbstractUser):
    """Модель Юзера."""
    email = models.EmailField(
        unique=True,
        max_length=254,
        null=False,
        verbose_name='email',
    )
    username = models.CharField(
        unique=True,
        validators=(validate_name,),
        max_length=150,
        null=False,
        verbose_name='имя пользователя'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=False,
        verbose_name='имя'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=False,
        verbose_name='фамилия'
    )
    password = models.CharField(
        verbose_name='пароль',
        max_length=128,
        null=False,
        blank=True,
    )
    last_login = models.DateTimeField(
        verbose_name='последний вход в систему',
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='активный'
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='Суперпользователь'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: tuple = (
        'username',
        'first_name',
        'last_name',
    )

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователь'
        ordering: tuple = ('username',)

    def __str__(self) -> str:
        return f'{self.username}'
