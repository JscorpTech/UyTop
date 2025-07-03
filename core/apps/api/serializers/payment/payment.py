from rest_framework import serializers

from core.apps.api.models import PaymentModel


class BasePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = [
            "id",
            "name",
        ]


class ListPaymentSerializer(BasePaymentSerializer):
    class Meta(BasePaymentSerializer.Meta): ...


class RetrievePaymentSerializer(BasePaymentSerializer):
    class Meta(BasePaymentSerializer.Meta): ...


class CreatePaymentSerializer(BasePaymentSerializer):
    class Meta(BasePaymentSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
