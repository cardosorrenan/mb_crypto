import json

import pytest
from rest_framework import status

from currency_api.services.mercado_bitcoin import MarketplaceService
from currency_api.utils import (
    get_mocked_currency_info_response,
    simulate_browser_headers,
)

pytestmark = pytest.mark.django_db


@pytest.mark.integration
class TestMarketplaceService:
    service = MarketplaceService()

    def test_get_product_successful_response(
        self, currency_instance, requests_get_mocked
    ):
        params = {"symbol": currency_instance.symbol}

        requests_get_mocked.return_value.status_code = status.HTTP_200_OK
        requests_get_mocked.return_value.json.return_value = (
            get_mocked_currency_info_response()
        )

        result, http_status = self.service.get_product(params)

        requests_get_mocked.assert_called_once_with(
            self.service.BASE_ENDPOINT + "product/unlogged",
            headers=simulate_browser_headers(),
        )

        assert http_status == status.HTTP_200_OK
        assert result == get_mocked_currency_info_response()

    def test_get_product_validation_error(self):
        params = {"symbol": "XYZ"}
        _, http_status = self.service.get_product(params)
        assert http_status == status.HTTP_400_BAD_REQUEST
