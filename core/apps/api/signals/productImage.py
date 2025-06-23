from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ProductimageModel


@receiver(post_save, sender=ProductimageModel)
def ProductimageSignal(sender, instance, created, **kwargs): ...
