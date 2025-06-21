from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import PropertyModel


@register(PropertyModel)
class PropertyTranslation(TranslationOptions):
    fields = []
