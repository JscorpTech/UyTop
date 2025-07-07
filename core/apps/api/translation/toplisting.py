from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ToplistingpriceModel


@register(ToplistingpriceModel)
class ToplistingpriceTranslation(TranslationOptions):
    fields = []
