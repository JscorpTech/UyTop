"""
Accounts app urls
"""

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterView, ResetPasswordView, MeView, ChangePasswordView, UsersCountAPIView
from rest_framework.routers import DefaultRouter
from .views.jwt_token import TelegramTokenObtainView

router = DefaultRouter()
router.register("auth", RegisterView, basename="auth")
router.register("auth", ResetPasswordView, basename="reset-password")
router.register("auth", MeView, basename="me")
router.register("auth", ChangePasswordView, basename="change-password")


urlpatterns = [
    path("", include(router.urls)),
    path('api/users/count/', UsersCountAPIView.as_view(), name='users-count'),
    path("auth/token/", TelegramTokenObtainView.as_view(), name="token_obtain_pair"),
    path("auth/token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path(
        "auth/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
