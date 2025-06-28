from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ResidentialcomplexModel


@receiver(post_save, sender=ResidentialcomplexModel)
def ResidentialcomplexSignal(sender, instance, created, **kwargs): ...
