from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import CategoryModel


@receiver(post_save, sender=CategoryModel)
def CategorySignal(sender, instance, created, **kwargs): ...
