from datetime import datetime

from django.conf import settings
from django.core.cache import cache
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import CurrencyModel
from .serializers import CurrencySerializer
from .services.alphavant import CurrencyExchangeRate
from .services.mercado_bitcoin import MarketplaceService

mb_integration = MarketplaceService()
alphavant_integration = CurrencyExchangeRate()


class CurrencyViewSet(GenericAPIView):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer
    CACHE_TIMEOUT_COIN_INFO = settings.DEFAULT_CACHE_TIME / 60 * 3
    http_method_names = ["post"]

    def transform_json(self, input_json: dict) -> dict:
        response_data = input_json.get("response_data", {})
        products = response_data.get("products", [{}])

        first_product = products[0]

        coin_name = first_product.get("name", "")
        symbol = first_product.get("product_id", "")
        coin_price_brl = float(first_product.get("market_price", 0))
        response_exchange = alphavant_integration.get_exchange_rate("BRL", "USD")
        rate_brl_usd = float(
            response_exchange["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        )
        coin_price_usd = float(coin_price_brl * rate_brl_usd)

        date_consult = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output_dict = {
            "coin_name": coin_name,
            "symbol": symbol,
            "coin_price": coin_price_brl,
            "coin_price_dolar": coin_price_usd,
            "date_consult": date_consult,
        }

        return output_dict

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
