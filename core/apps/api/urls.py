from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import ListingView, ListingimageView, CategoryView, AmenityView


router = DefaultRouter()
router.register(r"listing", ListingView, basename="listing")
router.register(r"listing-image", ListingimageView, basename="Listingimage")

router.register("category", CategoryView, basename="category")
router.register("amenity", AmenityView, basename="amenity")



urlpatterns = [
    path("", include(router.urls)),
]
