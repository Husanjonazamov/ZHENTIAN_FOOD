from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import BannerModel


@admin.register(BannerModel)
class BannerAdmin(ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    list_display_links = ("title",)
