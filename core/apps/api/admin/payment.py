from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CheckModel, PaymentModel
from django.utils.html import format_html


@admin.register(PaymentModel)
class PaymentAdmin(ModelAdmin):
    list_display = (
        "id",
        "card_number",
        "card_owner",
        "top_price",
        "listing_price",
    )
    list_display_links = ("card_number",)


@admin.register(CheckModel)
class CheckAdmin(ModelAdmin):
    list_display = (
        "image_tag",
        "id",
        "created_at",
    )
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="70" height="70" style="object-fit: cover;" />', obj.image.url)
        return "-"
    
    image_tag.short_description = "Rasm"
