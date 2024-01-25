import os

import requests


class CurrencyExchangeRate:
    ALPHAVANT_API_KEY = os.environ.get("ALPHAVANT_API_KEY")
    BASE_ENDPOINT = os.environ.get("ALPHAVANT_QUERY_URL")

    @staticmethod
    def get_exchange_rate(from_currency: str, to_currency: str) -> dict:
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
            "apikey": CurrencyExchangeRate.ALPHAVANT_API_KEY,
        }

        response = requests.get(CurrencyExchangeRate.BASE_ENDPOINT, params=params)
        return response.json()
