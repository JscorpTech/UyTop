# mixins.py
from rest_framework import serializers




class CurrencyPriceMixin(serializers.Serializer):
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        request = self.context.get("request")
        currency = request.headers.get("currency", "UZS").upper()

        field_map = {
            "UZS": "price_uzs",
            "SHB": "price_shb",
        }

        field_name = field_map.get(currency, "price_uzs")
        return getattr(obj, field_name, None)
