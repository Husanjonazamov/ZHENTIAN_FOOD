from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline

from core.apps.api.models import OptionsModel
from core.apps.api.admin.optionValue import OptionValueInline
    
    
    
@admin.register(OptionsModel)
class OptionsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = [OptionValueInline]
    

