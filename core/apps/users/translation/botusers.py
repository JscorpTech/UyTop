from modeltranslation.translator import TranslationOptions, register

from core.apps.users.models import BotusersModel


@register(BotusersModel)
class BotusersTranslation(TranslationOptions):
    fields = []
