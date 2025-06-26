from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
import os 
from django_ckeditor_5.fields import CKEditor5Field


def load_default_description():
    file_path = os.path.join('/code', 'resources', 'templates', 'defaults', 'description_default.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

class ProductModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    subtitle = models.CharField(verbose_name=_("Subtitle"), max_length=200, blank=True, null=True)
    category = models.ForeignKey("api.CategoryModel", on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"),blank=True, null=True)
    content = models.TextField(verbose_name=_("Content"), blank=True, null=True)
    image = models.ImageField(verbose_name=_("Image"), upload_to="product/", blank=True, null=True)
    link = models.URLField(verbose_name=_("Youtube Link"), blank=True, null=True)
    table = CKEditor5Field(config_name="default", default=load_default_description)
    popular = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    rate = models.FloatField(default=0.0)
    
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
