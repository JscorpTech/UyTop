from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ListingModel, ListingsubtypeModel


@register(ListingModel)
class ListingTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(ListingsubtypeModel)
class ListingsubtypeTranslation(TranslationOptions):
    fields = ["name"]
