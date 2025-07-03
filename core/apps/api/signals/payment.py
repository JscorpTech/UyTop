from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import CheckModel, PaymentModel


@receiver(post_save, sender=PaymentModel)
def PaymentSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=CheckModel)
def CheckSignal(sender, instance, created, **kwargs): ...
