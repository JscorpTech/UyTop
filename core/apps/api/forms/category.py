from django import forms

from core.apps.api.models import CategoryModel


class CategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryModel
        fields = "__all__"
