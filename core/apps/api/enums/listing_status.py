from datetime import date, timedelta

def check_and_update_top_status(obj):
    today = date.today()
    changed = False

    if obj.is_top and obj.top_start_date and obj.listing.toplisting.day:
        expire_top_date = obj.top_start_date + timedelta(days=obj.listing.toplisting.day)
        if today >= expire_top_date:
            obj.is_top = False
            changed = True

    if obj.is_active and obj.top_start_date:
        expire_active_date = obj.top_start_date + timedelta(days=30)
        if today >= expire_active_date:
            obj.is_active = False
            changed = True

    if changed:
        obj.save()
