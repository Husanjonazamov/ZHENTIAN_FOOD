from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ProductModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    subtitle = models.CharField(verbose_name=_("Subtitle"), max_length=200, blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"),blank=True, null=True),
    content = models.TextField(verbose_name=_("Content"), blank=True, null=True)
    image = models.ImageField(verbose_name=_("Image"), upload_to="product/", blank=True, null=True)
    
    
    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "product"
        verbose_name = _("ProductModel")
        verbose_name_plural = _("ProductModels")
