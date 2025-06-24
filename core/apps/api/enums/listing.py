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
    TOTAL = "total", _("Umumiy Narx"),
    SQUARE = "square",_("Narx m2")
    
    
class CurrencyChoice(models.TextChoices):
    UZS = "uzs", _("So'm")
    USD = "shb", _("Sh.b")