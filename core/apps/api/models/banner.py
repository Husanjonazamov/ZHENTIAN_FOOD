from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BannerModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    subtitle = models.CharField(verbose_name=_("Subtitle"), max_length=250)
    image = models.ImageField(verbose_name=_("Image"), upload_to="banner/")
    
    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "banner"
        verbose_name = _("BannerModel")
        verbose_name_plural = _("BannerModels")
