from django import forms

from core.apps.api.models import ResidentialcomplexModel


class ResidentialcomplexForm(forms.ModelForm):

    class Meta:
        model = ResidentialcomplexModel
        fields = "__all__"
