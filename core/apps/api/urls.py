from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    BannerView,
    CategoryView,
    ProductView,
    OptionsView
)

router = DefaultRouter()
router.register(r"banner", BannerView, basename="banner")
router.register(r"category", CategoryView, basename="category")
router.register(r"products", ProductView, basename="product")
router.register(r"options", OptionsView, basename="options")


urlpatterns = [
    path("", include(router.urls)),
]
