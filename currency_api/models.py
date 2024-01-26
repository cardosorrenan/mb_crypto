from django.db import models


class CurrencyModel(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} - {self.symbol}"
