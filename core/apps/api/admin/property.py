from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import PropertyModel


@admin.register(PropertyModel)
class PropertyAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name"),
    
