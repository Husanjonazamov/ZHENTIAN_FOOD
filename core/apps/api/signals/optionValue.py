from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import OptionvalueModel


@receiver(post_save, sender=OptionvalueModel)
def OptionvalueSignal(sender, instance, created, **kwargs): ...
