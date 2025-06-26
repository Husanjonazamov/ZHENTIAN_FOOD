from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CategoryModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("title"), max_length=255)
    image = models.ImageField(verbose_name=_("Image"), upload_to="category/", blank=True, null=True)
    url = models.URLField(verbose_name=_("Url"), blank=True, null=True)
    
    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")
