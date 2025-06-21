from django import forms

from core.apps.api.models import DistrictModel


class DistrictForm(forms.ModelForm):

    class Meta:
        model = DistrictModel
        fields = "__all__"
