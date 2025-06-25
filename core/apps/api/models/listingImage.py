from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class ListingimageModel(AbstractBaseModel):
    listing = models.ForeignKey(
        "api.ListingModel",
        on_delete=models.CASCADE,
        verbose_name=_("Uy elonlari"),
        related_name="images",
        blank=True, null=True
    )
    image = models.ImageField(verbose_name=_("Rasmlar"), upload_to="listing/", blank=True, null=True)

    def __str__(self):
        return str(self.listing.name)


    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "ListingImage"
        verbose_name = _("ListingimageModel")
        verbose_name_plural = _("ListingimageModels")
