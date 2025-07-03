from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import PaymentModel


@admin.register(PaymentModel)
class PaymentAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
