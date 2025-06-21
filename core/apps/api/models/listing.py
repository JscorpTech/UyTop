from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ListingModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "listing"
        verbose_name = _("ListingModel")
        verbose_name_plural = _("ListingModels")


class ListingsubtypeModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)


    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "listingSubType"
        verbose_name = _("ListingsubtypeModel")
        verbose_name_plural = _("ListingsubtypeModels")
