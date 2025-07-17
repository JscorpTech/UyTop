from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline as UnfoldTabulerAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import ListingModel, ListingimageModel



class ListingImageInlines(UnfoldTabulerAdmin):
    model = ListingimageModel
    extra = 5



from django.utils.html import format_html

@admin.register(ListingModel)
class ListingAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
        "dealtype",
        "floor",
        "is_active",
        "repair_type",
        "building",
        "show_images"  # Rasmlarni chiqaradigan method
    )
    inlines = [ListingImageInlines]
    list_display_links = ("name",)

    def show_images(self, obj):
        images = obj.images.all()[:3]  # Faqat 3 ta rasm ko‘rsatish uchun
        imgs = ""
        for img in images:
            imgs += f'<img src="{img.image.url}" width="50" style="margin-right:5px;" />'
        return format_html(imgs)
    
    show_images.short_description = "Rasmlar"


    
    
