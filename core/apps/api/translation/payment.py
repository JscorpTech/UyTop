from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import PaymentModel


@register(PaymentModel)
class PaymentTranslation(TranslationOptions):
    fields = []
