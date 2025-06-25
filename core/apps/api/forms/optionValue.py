from django import forms

from core.apps.api.models import OptionvalueModel


class OptionvalueForm(forms.ModelForm):

    class Meta:
        model = OptionvalueModel
        fields = "__all__"
