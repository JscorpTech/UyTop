from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import AmenityModel


@admin.register(AmenityModel)
class AmenityAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
