from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BotusersModel(AbstractBaseModel):
    first_name = models.CharField(verbose_name=_("first_name"), max_length=255)
    last_name = models.CharField(verbose_name=_("last_name"), max_length=200)
    photo_url = models.TextField(verbose_name=_("Photo url"))
    tg_id = models.BigIntegerField(verbose_name=_("Tg id"), unique=True)
    

    def __str__(self):
        return str(self.first_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "botusers"
        verbose_name = _("BotusersModel")
        verbose_name_plural = _("BotusersModels")
