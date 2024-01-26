import json
import re
from datetime import datetime
from typing import Dict

from currency_api.models import CurrencyModel
from currency_api.services.alphavant import CurrencyExchangeRate

alphavant_integration = CurrencyExchangeRate()


class CurrencyValidator:
    VALID_SYMBOL_REGEX = r"^[a-zA-Z0-9]{3}$"

    def checker(self, symbol: str) -> dict or None:
        if not symbol:
            return "Symbol is required"

        if not re.match(self.VALID_SYMBOL_REGEX, symbol):
            return f"Symbol is in the wrong format: {symbol}"

        if not CurrencyModel.objects.filter(symbol=symbol).exists():
            return "Symbol not found"

        return None


def get_exchange_rate() -> float:
    response_exchange = alphavant_integration.get_exchange_rate("BRL", "USD")
    return float(
        response_exchange["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )


def format_currency_info_response(input_json: Dict) -> Dict:
    response_data = input_json.get("response_data", {})
    products = response_data.get("products", [{}])
    first_product = products[0]

    coin_name = first_product.get("name", "")
    symbol = first_product.get("product_id", "")
    coin_price_brl = float(first_product.get("market_price", 0))

    coin_price_usd = coin_price_brl * get_exchange_rate()
    date_consult = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "coin_name": coin_name,
        "symbol": symbol,
        "coin_price": coin_price_brl,
        "coin_price_dolar": coin_price_usd,
        "date_consult": date_consult,
    }


def simulate_browser_headers() -> dict:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    }
    return headers


def get_mocked_currency_info_response():
    CURRENCY_INFO_MOCKED_DATA = (
        "currency_api/services/mocked_data/mb_marketplace_btc.json"
    )

    with open(CURRENCY_INFO_MOCKED_DATA, "r") as json_file:
        return json.load(json_file)
