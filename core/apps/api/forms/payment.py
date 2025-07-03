from django import forms

from core.apps.api.models import PaymentModel


class PaymentForm(forms.ModelForm):

    class Meta:
        model = PaymentModel
        fields = "__all__"
