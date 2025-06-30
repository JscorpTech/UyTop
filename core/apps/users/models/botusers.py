from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BotusersModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Ism"), max_length=255)
    tg_id = models.BigIntegerField(verbose_name=_("Tg id"), blank=True, null=True)
    

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "botusers"
        verbose_name = _("BotusersModel")
        verbose_name_plural = _("BotusersModels")
