from factory import Faker
from factory.django import DjangoModelFactory

from currency_api.models import CurrencyModel


class CurrencyFactory(DjangoModelFactory):
    name = Faker("name")
    symbol = Faker("bothify", text="???")

    class Meta:
        model = CurrencyModel
