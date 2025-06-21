from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class PropertyModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "Property"
        verbose_name = _("PropertyModel")
        verbose_name_plural = _("PropertyModel")




class PropertysubtypeModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    type = models.ForeignKey(PropertyModel, on_delete=models.CASCADE, verbose_name=_("Turi"))


    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "Propertysubtype"
        verbose_name = _("PropertysubtypeModel")
        verbose_name_plural = _("PropertysubtypeModel")
