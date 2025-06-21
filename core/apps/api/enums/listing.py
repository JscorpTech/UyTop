from django.db import models
from django.utils.translation import gettext_lazy as _



class DealTypeChoice(models.TextChoices):
    SALE = "sale", _("Sotiladi")
    RENT = "rent", _("Ijaraga beriladi")
    
    
    