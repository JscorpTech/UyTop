from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from core.apps.api.models import DistrictModel


@admin.register(DistrictModel)
class DistrictAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name"),
    
