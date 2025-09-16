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
    from django.utils import timezone
    from datetime import timedelta

    listing = ListingModel.objects.get(id=listing_id)
    if listing.is_top and listing.top_start_date and getattr(listing.listing, 'toplisting', None):
        now = timezone.now()
        try:
            top_days = int(listing.listing.toplisting.day)
        except (ValueError, TypeError):
            top_days = 0

        expire_top_date = listing.top_start_date + timedelta(seconds=10)  
        print(f"Listing {listing_id} expire_top_date:", expire_top_date)

        if now >= expire_top_date:
            listing.is_top = False
            listing.save(update_fields=["is_top"])
            print(f"Listing {listing_id} top expired!")
