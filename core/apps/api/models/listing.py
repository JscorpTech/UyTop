from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.enums.listing import (
    DealTypeChoice,
    RepairTypeChoice,
    LandTypeChoices,
    PriceTypeChoice,
    CurrencyChoice   
)


class ListingModel(AbstractBaseModel):
    # === Asosiy ma'lumotlar ===
    name = models.CharField(_("Nomi"), max_length=255)
    dealtype = models.CharField(_("Bitim Turi"), max_length=100, choices=DealTypeChoice.choices, default=DealTypeChoice.RENT, blank=True, null=True)
    property = models.CharField(_("Mulk Turi"), max_length=200, blank=True, null=True)
    property_subtype = models.CharField(_("Turi"), max_length=200, blank=True, null=True)

    # === Turar joy turlari ===
    apartment_type = models.CharField(_("Kvartira turi"), max_length=100, blank=True, null=True)
    house_type = models.CharField(_("Uy turi"), max_length=100, blank=True, null=True)
    business_type = models.CharField(_("Biznes turi"), max_length=100, blank=True, null=True)
    land_type = models.CharField(_("Yer turi"), choices=LandTypeChoices.choices, default=LandTypeChoices.RESIDENTIAL, max_length=100, blank=True, null=True)
    residential_complex = models.CharField(_("Turar joy majmuasi"), max_length=255, blank=True, null=True)

    # === Geolokatsiya ===
    latitude = models.FloatField(_("Kenglik"), blank=True, null=True)
    longitude = models.FloatField(_("Uzunlik"), blank=True, null=True)
    address = models.CharField(_("Manzil"), max_length=255, blank=True, null=True)

    # === Xonalar va qavatlar ===
    room_count = models.PositiveSmallIntegerField(_("Xonalar soni"), blank=True, null=True)
    floor = models.PositiveSmallIntegerField(_("Nechinchi qavatda"))
    total_floors = models.PositiveSmallIntegerField(_("Binoni jami qavatlari"))
    floors_count = models.PositiveSmallIntegerField(_("Qavatlar soni"), blank=True, null=True)

    # === Maydonlar ===
    area = models.CharField(_("kv.metr"), max_length=200)
    apartment_area = models.FloatField(_("Kvartira maydoni"), blank=True, null=True)
    house_area = models.FloatField(_("Uy maydoni"), blank=True, null=True)
    land_area = models.FloatField(_("Yer maydoni"), blank=True, null=True)
    office_area = models.FloatField(_("Ofis maydoni"), blank=True, null=True)
    building_area = models.FloatField(_("Bino maydoni"), blank=True, null=True)
    construction_area = models.FloatField(_("Qurilish maydoni"), blank=True, null=True)
    room_area = models.FloatField(_("Xona maydoni"), blank=True, null=True)

    # === Remont va qurilish ===
    repair_type = models.CharField(_("Remont turi"), max_length=200, choices=RepairTypeChoice.choices, default=RepairTypeChoice.AUTHOR)
    building = models.ForeignKey("api.BuildingmaterialModel", on_delete=models.CASCADE, verbose_name=_("Qurilish Materiallari"), blank=True, null=True)
    # === Narx va valyuta ===
    price_type = models.CharField(_("Narx Turi"), max_length=100, choices=PriceTypeChoice.choices, default=PriceTypeChoice.TOTAL)
    price_uzs = models.DecimalField(_("Narx (UZS)"), max_digits=15, decimal_places=2)
    price_shb = models.DecimalField(_("Narx (Sh.B.)"), max_digits=15, decimal_places=2)
    currency = models.CharField(_("Valyuta Turi"), max_length=10, choices=CurrencyChoice.choices, default=CurrencyChoice.UZS)
    negotiable = models.BooleanField(_("Kelishiladi"), default=False)

    # === Qo‘shimcha ===
    description = models.TextField(_("Ochiqlama"), blank=True, null=True)
    phone = models.CharField(_("Telefon"), max_length=50, blank=True, null=True)
    amenity = models.ManyToManyField("api.AmenityModel", verbose_name=_("Quylaylik"), blank=True, null=True)


    def __str__(self):
        return str(self.name)




    @classmethod
    def _create_fake(cls):
        return cls.objects.create(name="mock")

    class Meta:
        db_table = "listing"
        verbose_name = _("ListingModel")
        verbose_name_plural = _("ListingModels")
