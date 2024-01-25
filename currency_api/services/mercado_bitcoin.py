import json
import os

import requests
from rest_framework import status

from currency_api.utils import CurrencyValidator, simulate_browser_headers

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

        try:
            response = requests.get(
                url,
                headers=simulate_browser_headers(),
            )

            response.raise_for_status()
            response = response.json()
        except Exception:
            json_file_path = "currency_api/services/mocked_data/mb_marketplace_btc.json"

            with open(json_file_path, "r") as json_file:
                response = json.load(json_file)

        return (
            response,
            status.HTTP_200_OK,
        )
