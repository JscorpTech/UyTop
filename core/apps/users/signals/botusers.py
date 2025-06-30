from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.users.models import BotusersModel


@receiver(post_save, sender=BotusersModel)
def BotusersSignal(sender, instance, created, **kwargs): ...
