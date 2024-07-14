from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import (
    # OpenApiParameter,
    extend_schema,
    extend_schema_view,
)


@extend_schema(
    tags=["Пользователь"],
    methods=["GET", "POST", "DELETE"],
    description="Все пользователи",
)
@extend_schema_view(
    list=extend_schema(
        summary="Получить список пользователей",
    ),
    retrieve=extend_schema(
        summary="Детальная информация о пользователе",
    ),
    create=extend_schema(
        summary="Создание пользователя",
    ),
    destroy=extend_schema(
        summary="Удаление пользователя",
    ),
)
class CustomUserViewset(UserViewSet):
    def get_permissions(self) -> list:
        if self.action == "me":
            self.permission_classes: tuple = (IsAuthenticated,)
        return super().get_permissions()
