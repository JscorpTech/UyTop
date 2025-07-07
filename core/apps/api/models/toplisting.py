from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ToplistingpriceModel(AbstractBaseModel):
    day = models.CharField(verbose_name=_("Kun"), max_length=255)
    price = models.CharField(verbose_name=_("Narx"), max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.day)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "TopListingPrice"
        verbose_name = _("ToplistingpriceModel")
        verbose_name_plural = _("ToplistingpriceModels")
