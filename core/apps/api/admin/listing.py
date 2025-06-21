from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import ListingModel


@admin.register(ListingModel)
class ListingAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    
    list_display_links = ("name"),



    
    
