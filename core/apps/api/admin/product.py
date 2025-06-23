from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
