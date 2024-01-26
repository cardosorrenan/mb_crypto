import pytest

from currency_api.utils import CurrencyValidator

pytestmark = pytest.mark.django_db

currency_validator = CurrencyValidator()


@pytest.mark.unit
class TestCurrencyValidator:
    def test_currency_validator_valid_symbol(self, currency_instance):
        result = currency_validator.checker(currency_instance.symbol)
        assert result is None

    def test_currency_validator_invalid_symbol_format(self):
        symbol = "US Dollar"
        result = currency_validator.checker(symbol)
        assert result == f"Symbol is in the wrong format: {symbol}"

    def test_currency_validator_symbol_not_found(self):
        symbol = "XYZ"
        result = currency_validator.checker(symbol)
        assert result == "Symbol not found"

    def test_currency_validator_empty_symbol(self):
        symbol = ""
        result = currency_validator.checker(symbol)
        assert result == "Symbol is required"
