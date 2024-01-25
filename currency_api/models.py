from django.db import models


class CurrencyModel(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name} - {self.code}"
