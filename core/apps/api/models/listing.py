from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.enums.listing import DealTypeChoice


class ListingModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    dealtype = models.CharField(
        verbose_name=_("Bitim Turi"),
        max_length=100,
        choices=DealTypeChoice.choices,
        default=DealTypeChoice.RENT,
        blank=True, null=True
    )

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "listing"
        verbose_name = _("ListingModel")
        verbose_name_plural = _("ListingModels")

