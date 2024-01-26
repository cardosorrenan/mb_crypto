import os

import requests
from rest_framework import status

from currency_api.utils import (
    CurrencyValidator,
    format_currency_info_response,
    get_mocked_currency_info_response,
    simulate_browser_headers,
)

validator = CurrencyValidator()


class MarketplaceService:
    BASE_ENDPOINT = os.environ.get("MB_MARKETPLACE_URL")

    def get_product(self, params: dict) -> tuple:
        url = self.BASE_ENDPOINT + "product/unlogged"

        validation_errors_result = validator.checker(params.get("symbol", ""))

        if validation_errors_result:
            return (
                {"error": validation_errors_result},
                status.HTTP_400_BAD_REQUEST,
            )

        response = requests.get(
            url,
            headers=simulate_browser_headers(),
        )

        # For local development purposes only
        if response.status_code == status.HTTP_403_FORBIDDEN:
            response = get_mocked_currency_info_response()
        else:
            response = response.json()

        return (
            format_currency_info_response(response),
            status.HTTP_200_OK,
        )
