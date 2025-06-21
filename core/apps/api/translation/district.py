from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import DistrictModel


@register(DistrictModel)
class DistrictTranslation(TranslationOptions):
    fields = []
