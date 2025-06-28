from django import forms

from core.apps.api.models import BuildingmaterialModel


class BuildingmaterialForm(forms.ModelForm):

    class Meta:
        model = BuildingmaterialModel
        fields = "__all__"
