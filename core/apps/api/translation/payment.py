from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CheckModel, PaymentModel


@register(PaymentModel)
class PaymentTranslation(TranslationOptions):
    fields = []


@register(CheckModel)
class CheckTranslation(TranslationOptions):
    fields = []
