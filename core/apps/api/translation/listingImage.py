from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ListingimageModel


@register(ListingimageModel)
class ListingimageTranslation(TranslationOptions):
    fields = []
