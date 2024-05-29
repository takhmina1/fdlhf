from rest_framework import serializers
from .models import CryptocurrencyData  # Assuming you have a model named CryptocurrencyData

class BinanceTickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptocurrencyData
        fields = ['symbol', 'bid_price', 'ask_price']  # Adjust fields according to your model
