from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import PropertyModel, PropertysubtypeModel


@register(PropertyModel)
class PropertyTranslation(TranslationOptions):
    fields = [
        "name"
    ]
    
    
@register(PropertysubtypeModel)
class PropertysubtypeTranslation(TranslationOptions):
    fields = [
        "name"
    ]

    

