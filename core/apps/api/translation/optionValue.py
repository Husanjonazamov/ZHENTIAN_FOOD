from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import OptionvalueModel


@register(OptionvalueModel)
class OptionvalueTranslation(TranslationOptions):
    fields = []
