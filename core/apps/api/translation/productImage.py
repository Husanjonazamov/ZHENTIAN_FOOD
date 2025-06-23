from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ProductimageModel


@register(ProductimageModel)
class ProductimageTranslation(TranslationOptions):
    fields = []
