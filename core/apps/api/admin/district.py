from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import DistrictModel


@admin.register(DistrictModel)
class DistrictAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
