from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ResidentialcomplexModel


@register(ResidentialcomplexModel)
class ResidentialcomplexTranslation(TranslationOptions):
    fields = [
        "name"
    ]
