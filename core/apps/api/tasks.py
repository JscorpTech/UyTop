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
        
        
    

@shared_task
def expire_top_listing(listing_id):
    print(f"\n\n{listing_id}\n\n")
    try:
        listing=ListingModel.objects.get(id=listing_id)
        listing.is_top = False
        print(listing.toplisting)
        listing.toplisting = None
        listing.top_start_date=None
        listing.save(update_fields=['is_top', 'toplisting', 'top_start_date'])
        print(f"{listing_id} ozgardi")
    except ListingModel.DoesNotExist:
        print(listing_id)
        
