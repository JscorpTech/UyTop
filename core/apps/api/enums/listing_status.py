from datetime import datetime, timedelta
from ..enums.listing import ListingStatus

from django.utils import timezone
from datetime import timedelta



from datetime import timedelta
from django.utils import timezone



def expire_listings():
    from core.apps.api.models.listing import ListingModel
    
    now = timezone.now()
    
    listings = ListingModel.objects.filter(is_active=True)
    
    for listing in listings:
        expire_date = listing.created_at + timedelta(days=30)
        if now >= expire_date:
            listing.status = ListingStatus.EXPIRED
            listing.is_active = False
            listing.save(update_fields=["status", "is_active"])
            print(f"Listing {listing.id} expired")





def check_and_update_top_status(listing_id=None):
    from core.apps.api.models.listing import ListingModel

    now = timezone.now()

    if listing_id:
        try:
            listings = [ListingModel.objects.get(id=listing_id)]
        except ListingModel.DoesNotExist:
            print(f"Listing ID {listing_id} topilmadi!")
            return
    else:
        listings = ListingModel.objects.filter(is_active=True)

    for listing in listings:
        if listing.is_top and listing.top_start_date and getattr(listing.listing, 'toplisting', None):
            expire_top_date = listing.top_start_date + timedelta(seconds=5)
            print("Listing top expire date:", expire_top_date)
            if now >= expire_top_date:
                listing.is_top = False
                listing.save(update_fields=["is_top"])
                print(f"Listing {listing.id} top expired!")


        
    if listing.is_active and listing.created_at:
        expire_active_date = listing.created_at + timedelta(seconds=5)
        print("created_at:", listing.created_at)
        print("expres:", expire_active_date)
        
        if timezone.now() >= expire_active_date:
            listing.status = ListingStatus.EXPIRED
            listing.is_active = False
            listing.save(update_fields=["status", "is_active"])
        else:
            print("Hali 10 sekund to‘lmadi, status o‘zgarmaydi.")
