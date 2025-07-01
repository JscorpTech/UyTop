from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()



class TelegramTokenObtainSerializer(serializers.Serializer):
    tg_id = serializers.IntegerField()
    first_name = serializers.CharField()

    def validate(self, attrs):
        tg_id = attrs.get("tg_id")
        first_name = attrs.get("first_name")

        try:
            user = User.objects.get(tg_id=tg_id)
        except User.DoesNotExist:
            raise AuthenticationFailed("Foydalanuvchi topilmadi.")

        if user.first_name != first_name:
            raise AuthenticationFailed("Ism noto‘g‘ri.")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    @classmethod
    def get_token(cls, user):
        return super().get_token(user)
