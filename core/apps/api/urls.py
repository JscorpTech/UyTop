from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import ListingView, ListingimageView

router = DefaultRouter()
router.register(r"listing", ListingView, basename="listing")
router.register(r"listing-image", ListingimageView, basename="Listingimage")



urlpatterns = [
    path("", include(router.urls)),
]
