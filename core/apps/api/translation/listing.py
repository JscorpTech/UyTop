from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ListingModel


@register(ListingModel)
class ListingTranslation(TranslationOptions):
    fields = [
        "name"
    ]

