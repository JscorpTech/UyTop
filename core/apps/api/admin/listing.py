from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ListingModel, ListingsubtypeModel


@admin.register(ListingModel)
class ListingAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(ListingsubtypeModel)
class ListingsubtypeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
