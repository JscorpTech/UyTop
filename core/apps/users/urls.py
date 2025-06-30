from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.users.views import BotusersView

router = DefaultRouter()
router.register("users", BotusersView, basename="botusers")


urlpatterns = [
    path("", include(router.urls)),
]
