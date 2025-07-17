from django.contrib import admin
from unfold.admin import ModelAdmin
from core.apps.api.models import ListingimageModel
from django.utils.safestring import mark_safe

@admin.register(ListingimageModel)
class ListingimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "listing",
        "image_tag",
    )

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height: 70px; border-radius: 8px; object-fit: cover;" />')
        return "-"
    
    image_tag.short_description = "Image"
