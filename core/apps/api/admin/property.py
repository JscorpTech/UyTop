from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import PropertyModel, PropertysubtypeModel


@admin.register(PropertyModel)
class PropertyAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name"),
    

@admin.register(PropertysubtypeModel)
class PropertysubtypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name"),