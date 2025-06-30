from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import FavoriteModel


@register(FavoriteModel)
class FavoriteTranslation(TranslationOptions):
    fields = []
