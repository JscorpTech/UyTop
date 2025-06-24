from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ListingimageModel


@admin.register(ListingimageModel)
class ListingimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
