from django import forms

from core.apps.api.models import ToplistingpriceModel


class ToplistingpriceForm(forms.ModelForm):

    class Meta:
        model = ToplistingpriceModel
        fields = "__all__"
