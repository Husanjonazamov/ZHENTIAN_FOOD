from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    list_display_links = ("title", )
