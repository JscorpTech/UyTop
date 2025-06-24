from django import forms

from core.apps.api.models import ListingimageModel


class ListingimageForm(forms.ModelForm):

    class Meta:
        model = ListingimageModel
        fields = "__all__"
