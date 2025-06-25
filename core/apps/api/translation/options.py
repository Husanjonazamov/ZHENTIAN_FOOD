from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import OptionsModel


@register(OptionsModel)
class OptionsTranslation(TranslationOptions):
    fields = []
