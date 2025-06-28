from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import BuildingmaterialModel


@receiver(post_save, sender=BuildingmaterialModel)
def BuildingmaterialSignal(sender, instance, created, **kwargs): ...
