from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ListingModel, ListingsubtypeModel


@receiver(post_save, sender=ListingModel)
def ListingSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=ListingsubtypeModel)
def ListingsubtypeSignal(sender, instance, created, **kwargs): ...
