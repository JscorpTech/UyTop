from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import ListingView

router = DefaultRouter()
router.register(r"listing", ListingView, basename="listing")



urlpatterns = [
    path("", include(router.urls)),
]
