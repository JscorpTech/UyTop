from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from core.apps.api.models import BuildingmaterialModel


@admin.register(BuildingmaterialModel)
class BuildingmaterialAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
    )
