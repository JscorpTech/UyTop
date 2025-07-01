from rest_framework_simplejwt.views import TokenViewBase
from core.apps.accounts.serializers.jwt_token import TelegramTokenObtainSerializer

class TelegramTokenObtainView(TokenViewBase):
    serializer_class = TelegramTokenObtainSerializer
