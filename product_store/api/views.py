from django.db.models import Sum

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response

from product.models import Product, Categories, SubCategories, ShoppingCart
from .serializers import (
    ProductSerializer,
    CategoriesSerializer,
    SubCategoriesSerializer,
    ShoppingCartReadSerializer,
    ShoppingCartWriteSerializer,
)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для Продуктов."""

    queryset: Product = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для Категорий."""

    queryset: Categories = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SubCategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для Подкатегорий."""

    queryset: SubCategories = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """Вьюсет для Корзины продуктов."""

    queryset: ShoppingCart = ShoppingCart.objects.all()
    permission_classes: tuple = (IsAuthenticated,)
    http_method_names = ["get", "post", "delete", "patch"]

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ShoppingCartReadSerializer
        return ShoppingCartWriteSerializer

    def list(self, request, *args, **kwargs):

        products = self.get_queryset()
        page = self.paginate_queryset(products)

        total_count = products.count()
        total_cost = (
            products.aggregate(Sum("product__price"))["product__price__sum"]
            or 0
        )

        if page is not None:
            serializer = self.get_serializer(products, many=True)
            return Response(
                {
                    "products": serializer.data,
                    "total_count": total_count,
                    "total_cost": total_cost,
                }
            )
        serializer = self.get_serializer(page, many=True)
        return Response(
            {
                "products": serializer.data,
                "total_count": total_count,
                "total_cost": total_cost,
            }
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=False, methods=["delete"])
    def clear(self, request):
        ShoppingCart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
