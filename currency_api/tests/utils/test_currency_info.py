import pytest

from currency_api.services.alphavant import CurrencyExchangeRate
from currency_api.utils import (
    format_currency_info_response,
    get_mocked_currency_info_response,
)

alphavant_integration = CurrencyExchangeRate()


@pytest.mark.unit
def test_format_currency_info_response(monkeypatch):
    def mock_get_exchange_rate(*args, **kwargs):
        return {"Realtime Currency Exchange Rate": {"5. Exchange Rate": "1.2"}}

    monkeypatch.setattr(
        alphavant_integration, "get_exchange_rate", mock_get_exchange_rate
    )

    sample_input_json = get_mocked_currency_info_response()
    result = format_currency_info_response(sample_input_json)

    assert isinstance(result["coin_name"], str)
    assert isinstance(result["symbol"], str)
    assert isinstance(result["coin_price"], float)
    assert isinstance(result["coin_price_dolar"], float)
    assert isinstance(result["date_consult"], str)
