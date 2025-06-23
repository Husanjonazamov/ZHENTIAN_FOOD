from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from core.apps.api.models import ProductModel, ProductimageModel

class ProductImageInline(TabularInline):
    model = ProductimageModel
    extra = 2 
    



@admin.register(ProductModel)
class ProductAdmin(ModelAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "category"
    )
    list_display_links = ("title", )
    inlines = [ProductImageInline]
