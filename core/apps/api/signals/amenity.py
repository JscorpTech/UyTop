from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import AmenityModel


@receiver(post_save, sender=AmenityModel)
def AmenitySignal(sender, instance, created, **kwargs): ...
