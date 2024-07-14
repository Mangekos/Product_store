from typing import Any
from rest_framework import serializers

from product.models import Product, Categories, SubCategories, ShoppingCart


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализер Категорий."""

    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Categories
        fields: str = (
            "id",
            "name",
            "slug",
            "image",
            "sub_categories",
        )

    def get_sub_categories(self, obj) -> SubCategories.name:
        return SubCategoriesSerializer(obj.sub_categories, many=True).data


class SubCategoriesSerializer(serializers.ModelSerializer):
    """Сериализер Подкатегорий."""

    # category = serializers.SerializerMethodField()

    class Meta:
        model = SubCategories
        fields: str = (
            "id",
            "name",
            "slug",
            # "category",
            "image",
        )

    # def get_category(self, obj) -> Categories.name:
    #     return obj.category.name


class ProductSerializer(serializers.ModelSerializer):
    """Сериализер Продуктов."""

    category = serializers.SerializerMethodField()
    subcategory = SubCategoriesSerializer(read_only=True)
    image_mini = serializers.SerializerMethodField()
    image_medium = serializers.SerializerMethodField()
    image_large = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields: str = (
            "id",
            "name",
            "slug",
            "subcategory",
            "category",
            "price",
            "image",
            "image_mini",
            "image_medium",
            "image_large",
        )

    def get_category(
        self, obj
    ) -> serializers.ReturnList | Any | serializers.ReturnDict:
        return obj.subcategory.category.name

    def get_image_mini(self, obj):
        return obj.image_mini.url if obj.image_mini else None

    def get_image_medium(self, obj):
        return obj.image_medium.url if obj.image_medium else None

    def get_image_large(self, obj):
        return obj.image_large.url if obj.image_large else None


class ShoppingCartWriteSerializer(serializers.ModelSerializer):
    """Сериализер записи Корзины покупок."""

    class Meta:
        model = ShoppingCart
        fields: str = (
            "product",
            "quantity",
        )

    def validate(self, data):
        request = self.context.get("request")
        user = request.user
        method = request.method
        if data["quantity"] <= 0:
            raise serializers.ValidationError(
                "Количество должно быть больше нуля"
            )

        if method == "POST":
            if ShoppingCart.objects.filter(
                user=user, product=data["product"]
            ).exists():
                raise serializers.ValidationError("Рецепт уже добавлен!")
        return data

    def to_representation(self, instance):
        request = self.context.get("request")
        context = {"request": request}
        return ShoppingCartReadSerializer(
            instance=instance, context=context
        ).data


class ShoppingCartReadSerializer(serializers.ModelSerializer):
    """Сериализер чтения Корзины покупок."""

    class Meta:
        model = ShoppingCart
        fields: str = (
            "id",
            "user",
            "product",
            "quantity",
        )
