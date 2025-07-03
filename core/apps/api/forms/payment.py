from django import forms

from core.apps.api.models import CheckModel, PaymentModel


class PaymentForm(forms.ModelForm):

    class Meta:
        model = PaymentModel
        fields = "__all__"


class CheckForm(forms.ModelForm):

    class Meta:
        model = CheckModel
        fields = "__all__"
