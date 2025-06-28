from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BuildingmaterialModel


@register(BuildingmaterialModel)
class BuildingmaterialTranslation(TranslationOptions):
    fields = [
        "name"
    ]
