from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.enums.listing import (
    DealTypeChoice,
    RepairTypeChoice,
    PriceTypeChoice,
    CurrencyChoice,
    ListingStatus
)

from django.utils import timezone
from datetime import date


class ListingModel(AbstractBaseModel):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="listings",
        blank=True, null=True
    )
    name = models.CharField(_("Nomi"), max_length=255)

    dealtype = models.CharField(
        _("Bitim Turi"),
        max_length=100,
        choices=DealTypeChoice.choices,
        default=DealTypeChoice.RENT,
        blank=True,
        null=True
    )
    residential_complex = models.ForeignKey(
        "api.ResidentialcomplexModel",
        on_delete=models.CASCADE,
        verbose_name=_("Complex"),
        blank=True, null=True
    )

    property = models.CharField(
        _("Mulk Turi"),
        max_length=200,
        blank=True,
        null=True
    )

    property_subtype = models.CharField(
        _("Mulk quyi turi"),
        max_length=100,
        blank=True,
        null=True
    )
    # === Geolokatsiya ===
    latitude = models.FloatField(_("Kenglik"), blank=True, null=True)
    longitude = models.FloatField(_("Uzunlik"), blank=True, null=True)
    address = models.CharField(_("Manzil"), max_length=255, blank=True, null=True)

    # === Xonalar va qavatlar ===
    room_count = models.CharField(_("Xonalar soni"), max_length=100, blank=True, null=True)
    floor = models.CharField(_("Nechinchi qavatda"), max_length=100, blank=True, null=True)
    total_floors = models.CharField(_("Binoni jami qavatlari"), max_length=100, blank=True, null=True)
    floors_count = models.CharField(_("Qavatlar soni"), max_length=100, blank=True, null=True)

    # === Maydonlar ===
    apartment_area = models.FloatField(_("Kvartira maydoni"), blank=True, null=True)
    house_area = models.FloatField(_("Uy maydoni"), blank=True, null=True)
    land_area = models.FloatField(_("Yer maydoni"), blank=True, null=True)
    office_area = models.FloatField(_("Ofis maydoni"), blank=True, null=True)
    building_area = models.FloatField(_("Bino maydoni"), blank=True, null=True)
    construction_area = models.FloatField(_("Qurilish maydoni"), blank=True, null=True)
    room_area = models.FloatField(_("Xona maydoni"), blank=True, null=True)

    # === Remont va qurilish ===
    repair_type = models.CharField(
        _("Remont turi"),
        max_length=200,
        choices=RepairTypeChoice.choices,
        default=RepairTypeChoice.AUTHOR,
        blank=True,
        null=True
    )

    building = models.ForeignKey(
        "api.BuildingmaterialModel",
        on_delete=models.CASCADE,
        verbose_name=_("Qurilish Materiallari"),
        blank=True,
        null=True
    )

    # === Narx va valyuta ===
    price_type = models.CharField(
        _("Narx Turi"),
        max_length=100,
        choices=PriceTypeChoice.choices,
        default=PriceTypeChoice.TOTAL
    )
    price = models.CharField(_("Narx"), max_length=200, blank=True, null=True)
    currency = models.CharField(_("Valyuta"), max_length=100, choices=CurrencyChoice.choices, default=CurrencyChoice.UZS)
    negotiable = models.BooleanField(_("Kelishiladi"), default=False)

    # === Qo‘shimcha ===
    description = models.TextField(_("Ochiqlama"), blank=True, null=True)
    phone = models.CharField(_("Telefon"), max_length=50, blank=True, null=True)

    amenity = models.ManyToManyField(
        "api.AmenityModel",
        verbose_name=_("Quylaylik"),
        blank=True,
        null=True
    )
    is_top = models.BooleanField(verbose_name=_("Top elonmi ?"), default=False)
    is_active = models.BooleanField(verbose_name=_("Activmi ?"), default=False)
    
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=100,
        choices=ListingStatus.choices,
        default=ListingStatus.PENDING
    )
    toplisting = models.ForeignKey(
        "api.ToplistingpriceModel",
        on_delete=models.CASCADE,
        verbose_name=_("Top Elon kunlari"),
        blank=True, null=True
    )
    top_start_date = models.DateField(null=True, blank=True)
    top_end_date = models.DateField(null=True, blank=True)
    
    
    
    def check_top_status(self):
        today = date.today()
        if self.is_top and self.top_end_date and self.top_end_date <= today:
            self.is_top = False
            self.save()
    

    def __str__(self):
        return str(self.name)
    
    

    @classmethod
    def _create_fake(cls):
        return cls.objects.create(name="mock")

    class Meta:
        db_table = "listing"
        verbose_name = _("ListingModel")
        verbose_name_plural = _("ListingModels")
