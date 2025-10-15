from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import timedelta

from core.apps.api.models import ListingModel
from core.apps.api.tasks import expire_listing_task, expire_top_listing
from core.apps.api.enums.listing_status import ListingStatus







@receiver(post_save, sender=ListingModel)
def after_update_listing_top(sender, instance, created, **kwargs):
    try:
        listing = ListingModel.objects.get(id=instance.id)
        print(listing.toplisting.day)
        if listing.is_top and listing.toplisting:
            toplisting_obj = instance.toplisting
            toplisting_days = int(toplisting_obj.day)
            expire_time = instance.updated_at + timedelta(days=toplisting_days)
            expire_top_listing.apply_async(args=[instance.id], eta=expire_time)
            
            print(f"---------------------{instance.id}------------")
            expire_top_listing.apply_async(args=[instance.id], eta=expire_time)


            print(f"✅ [TOPLISTING] Listing {instance.id} {toplisting_days} kundan keyin tushadi ({expire_time})")

    except Exception as e:
        print(f"❌ [SIGNAL ERROR] {e}")

        
        


@receiver(post_save, sender=ListingModel)
def after_update_listing(sender, instance, created, **kwargs):
    if created:
        expire_time = instance.updated_at + timedelta(days=30)
        expire_listing_task.apply_async(args=[instance.id], eta=expire_time)
        print(f"⏳ [NEW] Task scheduled for Listing {instance.id} at {expire_time}")
        return

    old = getattr(instance, "_old_instance", None)
    if old and (old.is_active == False or old.status != ListingStatus.APPROVED):
        if instance.is_active and instance.status == ListingStatus.APPROVED:
            expire_time = instance.updated_at + timedelta(days=30)
            expire_listing_task.apply_async(args=[instance.id], eta=expire_time)
            print(f"⏳ [UPDATED] Task scheduled for Listing {instance.id} at {expire_time}")
