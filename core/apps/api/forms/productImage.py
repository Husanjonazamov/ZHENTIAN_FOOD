from django import forms

from core.apps.api.models import ProductimageModel


class ProductimageForm(forms.ModelForm):

    class Meta:
        model = ProductimageModel
        fields = "__all__"
