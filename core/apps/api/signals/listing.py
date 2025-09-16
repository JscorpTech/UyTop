from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ListingModel
from core.apps.api.tasks import expire_listing_task 



@receiver(post_save, sender=ListingModel)
def ListingSignal(sender, instance, created, **kwargs): 
    if created:
        expire_listing_task.apply_async(args=[instance.id], countdown=2592000)
        print(f"Celery task scheduled for Listing {instance.id}")

