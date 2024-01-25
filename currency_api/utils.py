import re

from currency_api.models import CurrencyModel


def simulate_browser_headers() -> dict:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    }
    return headers


class CurrencyValidator:
    VALID_SYMBOL_REGEX = r"^[a-zA-Z0-9]{3}$"

    @staticmethod
    def checker(symbol: str) -> dict or None:
        if not symbol:
            return "Symbol is required"

        if not re.match(CurrencyValidator.VALID_SYMBOL_REGEX, symbol):
            return f"Symbol is in the wrong format: {symbol}"

        if not CurrencyModel.objects.filter(symbol=symbol).exists():
            return "Symbol not found"

        return None
