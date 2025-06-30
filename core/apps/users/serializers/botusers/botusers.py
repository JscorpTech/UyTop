from rest_framework import serializers

from core.apps.users.models import BotusersModel


class BaseBotusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotusersModel
        fields = [
            "id",
            "name",
        ]


class ListBotusersSerializer(BaseBotusersSerializer):
    class Meta(BaseBotusersSerializer.Meta): ...


class RetrieveBotusersSerializer(BaseBotusersSerializer):
    class Meta(BaseBotusersSerializer.Meta): ...


class CreateBotusersSerializer(BaseBotusersSerializer):
    class Meta(BaseBotusersSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
