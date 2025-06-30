from rest_framework import serializers

from core.apps.users.models import BotusersModel


class BaseBotusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotusersModel
        fields = [
            "id",
            "name",
            "tg_id"
        ]


class ListBotusersSerializer(BaseBotusersSerializer):
    class Meta(BaseBotusersSerializer.Meta): ...


class RetrieveBotusersSerializer(BaseBotusersSerializer):
    class Meta(BaseBotusersSerializer.Meta): ...



class CreateBotusersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    tg_id = serializers.IntegerField(required=False)

    class Meta:
        model = BotusersModel
        fields = ["id", "name", "tg_id"]
        
        
    def create(self, validated_data):
        request = self.context.get("request")
        bot_user = getattr(request, "bot_user", None)
        
        if bot_user:
            return bot_user
        raise serializers.ValidationError("foydalanuvchi yoq")