from django import forms

from core.apps.api.models import FavoriteModel


class FavoriteForm(forms.ModelForm):

    class Meta:
        model = FavoriteModel
        fields = "__all__"
