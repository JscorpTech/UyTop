from django import forms

from core.apps.api.models import ListingModel, ListingsubtypeModel


class ListingForm(forms.ModelForm):

    class Meta:
        model = ListingModel
        fields = "__all__"


class ListingsubtypeForm(forms.ModelForm):

    class Meta:
        model = ListingsubtypeModel
        fields = "__all__"
