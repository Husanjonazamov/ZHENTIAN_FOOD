from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class OptionvalueModel(AbstractBaseModel):
    option_key = models.ForeignKey("api.OptionsModel", on_delete=models.CASCADE, blank=True, null=True)
    value = models.CharField(verbose_name=_("value"), max_length=255)

    
    def __str__(self):
        return str(self.value)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "optionValue"
        verbose_name = _("OptionvalueModel")
        verbose_name_plural = _("OptionvalueModels")
