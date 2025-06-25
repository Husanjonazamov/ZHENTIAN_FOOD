from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import OptionvalueModel



class OptionValueInline(admin.TabularInline):
    model = OptionvalueModel
    extra = 1


@admin.register(OptionvalueModel)
class OptionvalueAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
