from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.users.models import BotusersModel


@admin.register(BotusersModel)
class BotusersAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
