from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ToplistingpriceModel


@admin.register(ToplistingpriceModel)
class ToplistingpriceAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
