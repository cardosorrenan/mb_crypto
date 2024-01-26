from unittest.mock import MagicMock

import pytest

from currency_api.services.alphavant import CurrencyExchangeRate


@pytest.mark.integration
class TestAlphavantService:
    def test_get_exchange_rate(self, requests_get_mocked):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Realtime Currency Exchange Rate": {"5. Exchange Rate": "1.0"}
        }
        requests_get_mocked.return_value = mock_response

        result = CurrencyExchangeRate.get_exchange_rate("BRL", "USD")

        requests_get_mocked.assert_called_once_with(
            CurrencyExchangeRate.BASE_ENDPOINT,
            params={
                "function": "CURRENCY_EXCHANGE_RATE",
                "from_currency": "BRL",
                "to_currency": "USD",
                "apikey": CurrencyExchangeRate.ALPHAVANT_API_KEY,
            },
        )

        assert result == {
            "Realtime Currency Exchange Rate": {"5. Exchange Rate": "1.0"}
        }
