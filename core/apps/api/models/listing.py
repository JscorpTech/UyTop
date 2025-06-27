from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.enums.listing import (
    DealTypeChoice,
    RepairTypeChoice,
    BuildingMaterialChoice,
    PriceTypeChoice,
    CurrencyChoice   
)


class ListingModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Nomi"), max_length=255)
    dealtype = models.CharField(
        verbose_name=_("Bitim Turi"),
        max_length=100,
        choices=DealTypeChoice.choices,
        default=DealTypeChoice.RENT,
        blank=True, null=True
    )
    property = models.ForeignKey(
        "api.PropertyModel",
        on_delete=models.CASCADE,
        verbose_name=_("Mulk turi"),
        blank=True, null=True
    )
    
    latitude = models.FloatField(verbose_name=_("Kenglik"), blank=True, null=True)
    longitude = models.FloatField(verbose_name=_("Uzunlik"), blank=True, null=True)
    room_count = models.PositiveSmallIntegerField(verbose_name=_("Xonalar soni"), blank=True, null=True)
    area = models.CharField(verbose_name=_("kv.metr"), max_length=200)
    floor = models.PositiveSmallIntegerField(verbose_name=_("Nechinchi qavatda"))
    total_floors = models.PositiveSmallIntegerField(verbose_name=_("Binoni jami qavatlari"))
    
    repair_type = models.CharField(
        verbose_name=_("Remont turi"),
        max_length=200,
        choices=RepairTypeChoice.choices,
        default=RepairTypeChoice.AUTHOR
    )
    
    building = models.CharField(
        verbose_name=_("Qurilish Materiallari"),
        max_length=100,
        choices=BuildingMaterialChoice.choices,
        default=BuildingMaterialChoice.BRICK
    )
    price_type = models.CharField(
        verbose_name=_("Narx Turi"),
        max_length=100,
        choices=PriceTypeChoice.choices,
        default=PriceTypeChoice.TOTAL
    )
    price_uzs = models.DecimalField(_("Narx (UZS)"), max_digits=15, decimal_places=2)
    price_shb = models.DecimalField(_("Narx (Sh.B.)"), max_digits=15, decimal_places=2)
    
    currency = models.CharField(
        verbose_name=_("Valyuta Turi"),
        choices=CurrencyChoice.choices,
        max_length=10,
        default=CurrencyChoice.UZS
    )
    description = models.TextField(verbose_name=_("Ochiqlama"), blank=True, null=True)
    amenity = models.ManyToManyField(
        "api.AmenityModel",
        verbose_name=_("Quylaylik"),
        blank=True, null=True
    )
    phone = models.CharField(verbose_name=_("Telefon"), max_length=50, blank=True, null=True)



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

