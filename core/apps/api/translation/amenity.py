from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import AmenityModel


@register(AmenityModel)
class AmenityTranslation(TranslationOptions):
    fields = []
