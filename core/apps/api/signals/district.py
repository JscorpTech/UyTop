from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import DistrictModel


@receiver(post_save, sender=DistrictModel)
def DistrictSignal(sender, instance, created, **kwargs): ...
