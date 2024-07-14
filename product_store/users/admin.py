from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display: tuple = ("email", "username", "first_name", "last_name")
    list_filter: tuple = ("username", "email")
    search_fields: tuple = ("username", "email")
    ordering: tuple = ("username",)
    empty_value_display: str = "-пусто-"
