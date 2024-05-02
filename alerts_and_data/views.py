from django.shortcuts import redirect
from rest_framework import generics
from .models import Coin, Alert
from .serializers import CoinSerializer, AlertSerializer
# -
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



# Create your views here.
class CoinList(generics.ListAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class AlertCreateView(APIView):
    def post(self, request, format=None):
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlertsRetrieve(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class CoinSearch(APIView):
    def get(self, request, *args, **kwargs):
        coinSymbol = request.query_params.get('coinSymbol')

        if not coinSymbol:
            return Response("coinSymbol parameter is required.", status=status.HTTP_400_BAD_REQUEST)

        coins = Coin.objects.filter(coinSymbol__icontains=coinSymbol)
        
        if not coins:
            return Response("Coin not found.", status=status.HTTP_404_NOT_FOUND)

        serializer = CoinSerializer(coins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class DeleteAlertView(generics.DestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    lookup_field = 'pk'
