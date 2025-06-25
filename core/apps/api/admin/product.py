from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from core.apps.api.forms.product import ProductForm
from core.apps.api.models.options import OptionsModel
from core.apps.api.forms.options import OptionsForm

from core.apps.api.models import ProductModel, ProductimageModel





class ProductImageInline(TabularInline):
    model = ProductimageModel
    extra = 2 
    
    
    
class OptionsInline(TabularInline):
    model = OptionsModel
    extra = 3
    

@admin.register(ProductModel)
class ProductAdmin(ModelAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "category",
        "popular"
    )
    form = ProductForm
    list_display_links = ("title", )
    inlines = [ProductImageInline, OptionsInline]
