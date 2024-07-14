from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriesViewSet,
    SubCategoriesViewSet,
    ProductViewSet,
    ShoppingCartViewSet,
)


router = DefaultRouter()

router.register("categories", CategoriesViewSet, basename="categories")
router.register(
    "subcategories", SubCategoriesViewSet, basename="subcategories"
)
router.register("products", ProductViewSet, basename="products")
router.register("shopping_cart", ShoppingCartViewSet, basename="shopping_cart")


urlpatterns: list = [
    path("", include(router.urls)),
]
