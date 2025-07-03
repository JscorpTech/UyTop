from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CheckModel, PaymentModel


@admin.register(PaymentModel)
class PaymentAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CheckModel)
class CheckAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
