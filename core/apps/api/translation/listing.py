from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ListingModel, ListingsubtypeModel


@register(ListingModel)
class ListingTranslation(TranslationOptions):
    fields = []


@register(ListingsubtypeModel)
class ListingsubtypeTranslation(TranslationOptions):
    fields = []
