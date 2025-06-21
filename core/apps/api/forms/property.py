from django import forms

from core.apps.api.models import PropertyModel


class PropertyForm(forms.ModelForm):

    class Meta:
        model = PropertyModel
        fields = "__all__"
