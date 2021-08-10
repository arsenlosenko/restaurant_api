from random import Random
from rest_framework import urlpatterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import RestaurantCRUDViewSet

router = DefaultRouter()
router.register(r"restaurants", RestaurantCRUDViewSet, basename="restaurants")
urlpatterns = [
    path("", include(router.urls)),
]