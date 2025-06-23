from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ProductimageModel(AbstractBaseModel):
    product = models.ForeignKey("api.ProductModel", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(verbose_name=_("Image"), upload_to="product/images/", blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "productImage"
        verbose_name = _("ProductimageModel")
        verbose_name_plural = _("ProductimageModels")
