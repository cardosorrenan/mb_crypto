from django.urls import path
from rest_framework import routers

from .views import CurrencyInfoView

router = routers.DefaultRouter()

urlpatterns = [
    path("coin_info/", CurrencyInfoView.as_view(), name="currency_api"),
]
