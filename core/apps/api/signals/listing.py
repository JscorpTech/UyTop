from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ListingModel
from core.apps.api.tasks import expire_listing_task, expire_top_listing



@receiver(post_save, sender=ListingModel)
def ListingSignal(sender, instance, created, **kwargs): 
    if created:
        expire_listing_task.apply_async(args=[instance.id], countdown=2592000)
        print(f"Celery tasks scheduled for Listing {instance.id}")

        expire_top_listing.apply_async(args=[instance.id], countdown=10)

        print(f"Celery task scheduled for Top Listing {instance.id}")

