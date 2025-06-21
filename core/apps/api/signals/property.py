from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import PropertyModel


@receiver(post_save, sender=PropertyModel)
def PropertySignal(sender, instance, created, **kwargs): ...
