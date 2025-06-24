from django import forms

from core.apps.api.models import AmenityModel


class AmenityForm(forms.ModelForm):

    class Meta:
        model = AmenityModel
        fields = "__all__"
