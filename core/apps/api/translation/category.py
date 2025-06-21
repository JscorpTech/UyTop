from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CategoryModel


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = []
