from django import forms

from core.apps.api.models import OptionsModel


class OptionsForm(forms.ModelForm):
    
    class Meta:
        model = OptionsModel
        fields = "__all__"
        widgets = {
            'key': forms.TextInput(attrs={'placeholder': 'Masalan: Rang'}),
            'value': forms.TextInput(attrs={'placeholder': 'Masalan: Qora'}),
        }