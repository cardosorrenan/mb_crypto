from django.conf import settings
from django.core.cache import cache
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import CurrencyModel
from .services.alphavant import CurrencyExchangeRate
from .services.mercado_bitcoin import MarketplaceService

mb_integration = MarketplaceService()
alphavant_integration = CurrencyExchangeRate()


class CurrencyInfoView(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    CACHE_TIMEOUT_COIN_INFO = settings.DEFAULT_CACHE_TIME / 60 * 3
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        symbol = request.data.get("symbol")

        cache_key = f"coin_info_{symbol}"
        coin_info_cached = cache.get(cache_key, None)

        if coin_info_cached:
            return Response(coin_info_cached)

        params = {
            "symbol": symbol,
            "limit": 20,
            "offset": 0,
            "order": "desc",
            "sort": "release_date",
        }

        coin_info_response, status = mb_integration.get_product(params)

        if status != 200:
            error_message = coin_info_response
            return Response(data=error_message, status=status)

        result = self.transform_json(coin_info_response)

        cache.set(key=cache_key, value=result, timeout=self.CACHE_TIMEOUT_COIN_INFO)

        return Response(data=result, status=status)
