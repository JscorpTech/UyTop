from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ListingimageModel


@receiver(post_save, sender=ListingimageModel)
def ListingimageSignal(sender, instance, created, **kwargs): ...
