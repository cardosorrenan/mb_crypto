from django.urls import path
from rest_framework import routers

from . import views, yasg_schema

router = routers.DefaultRouter()

urlpatterns = [
    path("coin_info/", views.CurrencyInfoView.as_view(), name="currency_api"),
]

urlpatterns += yasg_schema.urls
