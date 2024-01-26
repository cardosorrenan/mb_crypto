from unittest.mock import patch

import pytest

from currency_api.tests.factories import CurrencyFactory


@pytest.fixture
def requests_get_mocked():
    with patch("requests.get") as mock_get:
        yield mock_get


@pytest.fixture
def currency_instance():
    yield CurrencyFactory.create()
