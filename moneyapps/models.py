from django.db import models

class CryptocurrencyData(models.Model):
    symbol = models.CharField(max_length=100)
    bid_price = models.DecimalField(max_digits=20, decimal_places=10)
    ask_price = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.symbol
