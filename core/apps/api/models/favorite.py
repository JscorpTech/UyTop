from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class FavoriteModel(AbstractBaseModel):
    user = models.ForeignKey(
        "users.BotusersModel",
        on_delete=models.CASCADE,
        related_name="favorite",
        blank=True, null=True 
    )
    listing = models.ForeignKey(
        "api.ListingModel",
        on_delete=models.CASCADE,
        verbose_name=_("elon")
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        unique_together = ["user", "listing"]
        db_table = "favorite"
        verbose_name = _("FavoriteModel")
        verbose_name_plural = _("FavoriteModels")
