from django.db import models
from django.utils.translation import gettext_lazy as _



class DealTypeChoice(models.TextChoices):
    SALE = "sale", _("Sotiladi")
    RENT = "rent", _("Ijaraga beriladi")
    


class RepairTypeChoice(models.TextChoices):
    AUTHOR = 'author', 'Avtorlik loyihasi'
    EURO = 'euro', 'Evrotamir'
    MEDIUM = 'medium', 'O‘rta'
    NEEDS_REPAIR = 'needs_repair', 'Ta’mir talab'
    BLACK_FINISH = 'black_finish', 'Qora suvoq'
    
    
    
class BuildingMaterialChoice(models.TextChoices):
    BRICK = 'brick', 'G‘isht'
    MONOLITH = 'monolith', 'Monolit'
    BLOCK = 'block', 'Beton bloklari'
    CONCRETE = 'concrete', 'Beton'
    OTHER = 'other', 'Boshqa'


class PriceTypeChoice(models.TextChoices):
    TOTAL = "total", _("Umumiy Narx")
    SQUARE = "square", _("Narx m2")
    SELL_PRICE = "salePrice", _("Narxi (Sotuv)")
    MONTHLY = "monthly", _("Oylik")
    DAILY = "daily", _("Kunlik")

    
class CurrencyChoice(models.TextChoices):
    UZS = "uzs", _("So'm")
    USD = "shb", _("Sh.b")
    
    

class LandTypeChoices(models.TextChoices):
    RESIDENTIAL = "residential", "Turar joy"
    NON_RESIDENTIAL = "non-residential", "Noturar joy"


class ListingStatus(models.TextChoices):
    PENDING = 'pending', 'Kutilmoqda'
    APPROVED = 'approved', 'Tasdiqlangan'
    REJECTED = 'rejected', 'Rad etilgan'