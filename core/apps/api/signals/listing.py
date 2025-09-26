from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import timedelta

from core.apps.api.models import ListingModel
from core.apps.api.tasks import expire_listing_task
from core.apps.api.enums.listing_status import ListingStatus


@receiver(pre_save, sender=ListingModel)
def before_update_listing(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._old_instance = ListingModel.objects.get(pk=instance.pk)
        except ListingModel.DoesNotExist:
            instance._old_instance = None


@receiver(post_save, sender=ListingModel)
def after_update_listing(sender, instance, created, **kwargs):
    if created:
        expire_time = instance.updated_at + timedelta(days=20)
        expire_listing_task.apply_async(args=[instance.id], eta=expire_time)
        print(f"⏳ [NEW] Task scheduled for Listing {instance.id} at {expire_time}")
        return

    old = getattr(instance, "_old_instance", None)
    if old and (old.is_active == False or old.status != ListingStatus.APPROVED):
        if instance.is_active and instance.status == ListingStatus.APPROVED:
            expire_time = instance.updated_at + timedelta(days=30)
            expire_listing_task.apply_async(args=[instance.id], eta=expire_time)
            print(f"⏳ [UPDATED] Task scheduled for Listing {instance.id} at {expire_time}")
