from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TableChoice(models.TextChoices):
    TABLE_ONE = "table1", _("Table 1")
    TABLE_TWO = "table2", _("Table 2")
    
    
class OptionsModel(AbstractBaseModel):
    product = models.ForeignKey(
        "api.ProductModel",
        on_delete=models.CASCADE,
        related_name="options",
        blank=True, null=True
    )
    table = models.CharField(
        verbose_name=_("Table"),
        max_length=200,
        choices=TableChoice.choices,
        default=TableChoice.TABLE_ONE    
    )
    key = models.CharField(verbose_name=_("Key"), max_length=200, blank=True, null=True)
    value = models.CharField(verbose_name=_("Value"), max_length=255, blank=True, null=True)  
    
    def __str__(self):
        return str(self.key)
    

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "OPtions"
        verbose_name = _("OptionsModel")
        verbose_name_plural = _("OptionsModels")

