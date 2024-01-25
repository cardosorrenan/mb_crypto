from django.urls import path
from rest_framework import routers

from .views import CurrencyViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path("coin_info/", CurrencyViewSet.as_view(), name="currency_api"),
]
