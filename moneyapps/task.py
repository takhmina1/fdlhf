from celery import shared_task
# from celery.task import periodic_task
from datetime import timedelta
from .models import CryptocurrencyData  # Assuming you have a model to store cryptocurrency data
import requests

# @shared_task
# def fetch_binance_data():
#     url = "https://api.binance.com/api/v3/ticker/bookTicker"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         # Process data and save it to your model
#         for item in data:
#             CryptocurrencyData.objects.create(symbol=item['symbol'], bid_price=item['bidPrice'], ask_price=item['askPrice'])
#     else:
#         print("Failed to fetch data from Binance API")

# @periodic_task(run_every=timedelta(seconds=60))
# def fetch_binance_data_periodic():
#     fetch_binance_data.delay()








# exchange/tasks.py
from celery import shared_task
from datetime import timedelta
from .models import CryptocurrencyData  # Assuming you have a model to store cryptocurrency data
import requests

@shared_task
def fetch_binance_data():
    url = "https://api.binance.com/api/v3/ticker/bookTicker"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Process data and save it to your model
        for item in data:
            CryptocurrencyData.objects.create(symbol=item['symbol'], bid_price=item['bidPrice'], ask_price=item['askPrice'])
    else:
        print("Failed to fetch data from Binance API")

@shared_task
def fetch_binance_data_periodic():
    fetch_binance_data.delay()
