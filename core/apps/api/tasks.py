# tasks.py
from celery import shared_task
from core.apps.api.models.listing import ListingModel
from core.apps.api.enums.listing_status import ListingStatus

@shared_task
def expire_listing_task(listing_id):
    try:
        listing = ListingModel.objects.get(id=listing_id)
        listing.status = ListingStatus.EXPIRED
        listing.is_active = False
        listing.save(update_fields=["status", "is_active"])
        print(f"Listing {listing_id} expired successfully!")
    except ListingModel.DoesNotExist:
        print(f"Listing {listing_id} does not exist.")