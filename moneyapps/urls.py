# exchange/urls.py
from django.urls import path
from .views import BinanceTickerView

urlpatterns = [
    path('binance-ticker/', BinanceTickerView.as_view(), name='binance-ticker'),
]
