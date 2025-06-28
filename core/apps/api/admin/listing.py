from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline as UnfoldTabulerAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import ListingModel, ListingimageModel



class ListingImageInlines(UnfoldTabulerAdmin):
    model = ListingimageModel
    extra = 5



@admin.register(ListingModel)
class ListingAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
        "dealtype",
        "floor",
        "total_floors",
        "repair_type",
        "building"
    )
    inlines = [ListingImageInlines]
    list_display_links = ("name"),



    
    
