from django.contrib import admin

from .models import ShoppingCart, Product, Categories, SubCategories


from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для модели Product"""

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:75px; max-height:75px"/>'.format(
                obj.image.url
            )
        )

    list_display: tuple = ("name", "slug", "subcategory", "image_tag")
    list_filter: tuple = ("name", "slug", "subcategory")
    search_fields: tuple = ("name", "slug", "subcategory")
    empty_value_display: str = "-пусто-"


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Админка для модели Categories"""

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:75px; max-height:75px"/>'.format(
                obj.image.url
            )
        )

    list_display: tuple = ("name", "slug", "image_tag")
    list_filter: tuple = ("name",)


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    """Админка для модели SubCategories"""

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:75px; max-height:75px"/>'.format(
                obj.image.url
            )
        )

    list_display: tuple = ("name", "slug", "category", "image_tag")
    list_filter: tuple = ("name",)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Админка для модели ShoppingCart"""

    list_display: tuple = (
        "user",
        "product",
    )
