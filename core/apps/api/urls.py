from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    ListingView,
    ListingimageView,
    CategoryView,
    AmenityView,
    PropertyView,
    PropertysubtypeView,
    BuildingmaterialView,
    ResidentialcomplexView,
    FavoriteView, PaymentView,CheckView
)


router = DefaultRouter()
router.register(r"listing", ListingView, basename="listing")
router.register(r"listing-image", ListingimageView, basename="Listingimage")

router.register(r"category", CategoryView, basename="category")
router.register(r"amenity", AmenityView, basename="amenity")
router.register(r"property", PropertyView, basename="property")
router.register(r"property-subtype", PropertysubtypeView, basename="propertysubtype")
router.register(r"building-material", BuildingmaterialView, basename="building-material")
router.register(r"residential-complex", ResidentialcomplexView, basename="residential-complex")
router.register(r"favorites", FavoriteView, basename="favorites")
router.register(r"payment", PaymentView, basename="payment")
router.register(r"check", CheckView, basename="check")



urlpatterns = [
    path("", include(router.urls)),
]
