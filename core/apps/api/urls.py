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
    FavoriteView, PaymentView, CheckView, ToplistingpriceView
)
from core.apps.api.views.top_listing import ListingIsTopView


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
router.register(r"toplistingprice", ToplistingpriceView, basename="toplistingprice")


urlpatterns = [
    path("", include(router.urls)),
    path("listing/top/<str:type>/<int:pk>/", ListingIsTopView.as_view(), name='listingistop'),
]
