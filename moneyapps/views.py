# from rest_framework import views
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import BinanceTickerSerializer
# from .tasks import fetch_binance_data

# # from .models import Purchase

# class BinanceTickerView(views.APIView):
#     def get(self, request):
#         # Fetch data from your database/model
#         # For demonstration, let's assume you have a CryptocurrencyData model
#         data = CryptocurrencyData.objects.all()
#         serializer = BinanceTickerSerializer(data, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         # Assuming the request body contains details for purchasing
#         # For example, {'symbol': 'BTCUSDT', 'quantity': 1, 'price': 50000}
#         symbol = request.data.get('symbol')
#         quantity = request.data.get('quantity')
#         price = request.data.get('price')

#         # Process purchase logic here
#         # For example, create a Purchase object
#         purchase = Purchase.objects.create(symbol=symbol, quantity=quantity, price=price)

#         # Return response
#         return Response({'message': 'Purchase successful'}, status=status.HTTP_201_CREATED)





# exchange/views.py
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .serializers import BinanceTickerSerializer
from .tasks import fetch_binance_data
from .models import Purchase

class BinanceTickerView(views.APIView):
    def get(self, request):
        # Fetch data from your database/model
        # For demonstration, let's assume you have a CryptocurrencyData model
        data = CryptocurrencyData.objects.all()
        serializer = BinanceTickerSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Assuming the request body contains details for purchasing
        # For example, {'symbol': 'BTCUSDT', 'quantity': 1, 'price': 50000}
        symbol = request.data.get('symbol')
        quantity = request.data.get('quantity')
        price = request.data.get('price')

        # Process purchase logic here
        # For example, create a Purchase object
        purchase = Purchase.objects.create(symbol=symbol, quantity=quantity, price=price)

        # Return response
        return Response({'message': 'Purchase successful'}, status=status.HTTP_201_CREATED)
