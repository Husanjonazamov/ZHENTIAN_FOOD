from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ProductimageModel


@admin.register(ProductimageModel)
class ProductimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
