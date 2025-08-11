from datetime import date, timedelta
from ..enums.listing import ListingStatus
from core.apps.api.models.listing import ListingModel

def check_and_update_top_status(obj):
    today = date.today()
    changed = False

    if obj.is_top and obj.top_start_date and obj.listing.toplisting.day:
        expire_top_date = obj.top_start_date + timedelta(days=obj.listing.toplisting.day)
        if today >= expire_top_date:
            obj.is_top = False
            changed = True

    for obj in ListingModel.objects.filter(is_active=True):
        if obj.created_at:
            expire_active_date = obj.created_at + timedelta(days=30)
            if today >= expire_active_date:
                obj.status = ListingStatus.EXPIRED
                obj.is_active = False
                obj.save(update_fields=["status", "is_active"])
    if changed:
        obj.save()
