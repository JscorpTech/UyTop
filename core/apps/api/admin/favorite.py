from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import FavoriteModel


@admin.register(FavoriteModel)
class FavoriteAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
