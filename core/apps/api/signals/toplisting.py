from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ToplistingpriceModel


@receiver(post_save, sender=ToplistingpriceModel)
def ToplistingpriceSignal(sender, instance, created, **kwargs): ...
