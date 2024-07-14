from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


from users.models import CustomUser


class Categories(models.Model):
    """Модель Категорий."""

    name = models.TextField(
        max_length=200, null=False, verbose_name="Название"
    )
    slug = models.CharField(
        max_length=200,
        null=False,
        verbose_name="Уникальный Слаг",
    )
    image = models.ImageField(upload_to="categories/", null=True, default=None)

    class Meta:
        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"
        ordering: tuple = ("name",)

    def __str__(self) -> str:
        return self.name


class SubCategories(models.Model):
    """Модель Подкатегорий."""

    name = models.CharField(
        max_length=200, unique=True, verbose_name="Название"
    )
    slug = models.CharField(
        max_length=200,
        null=False,
        verbose_name="Уникальный Слаг",
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="sub_categories",
    )
    image = models.ImageField(
        upload_to="sub_categories/", null=True, default=None
    )

    class Meta:
        verbose_name: str = "Подкатегория"
        verbose_name_plural: str = "Подкатегории"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """Модель Продукта."""

    name = models.CharField(
        max_length=200,
        verbose_name="Название",
    )
    slug = models.CharField(
        max_length=200,
        verbose_name="Уникальный Слаг",
    )
    image = models.ImageField(
        upload_to="products/",
        null=False,
        default=None,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена",
    )
    subcategory = models.ForeignKey(
        SubCategories,
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
        related_name="products",
    )
    image_mini = ImageSpecField(
        source="image",
        processors=[ResizeToFit(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    image_medium = ImageSpecField(
        source="image",
        processors=[ResizeToFit(300, 200)],
        format="JPEG",
        options={"quality": 70},
    )
    image_large = ImageSpecField(
        source="image",
        processors=[ResizeToFit(600, 400)],
        format="JPEG",
        options={"quality": 80},
    )

    class Meta:
        ordering: tuple = ("-id",)
        verbose_name: str = "Продукт"
        verbose_name_plural: str = "Продукты"

    def __str__(self) -> str:
        return self.name


class ShoppingCart(models.Model):
    """Модель Корзины покупок."""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="shopping_cart",
        verbose_name="Пользователь",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_in_cart",
        verbose_name="Продукт",
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name: str = "Покупки"
        verbose_name_plural: str = "Покупки"
        constraints: tuple = (
            UniqueConstraint(
                fields=["user", "product"], name="unique_shopping_cart"
            ),
        )

    def __str__(self) -> str:
        return f"{self.user} добавил {self.product} в корзину покупок"
