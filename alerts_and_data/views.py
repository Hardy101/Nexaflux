from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Coin, Alert
from .serializers import CoinSerializer, AlertSerializer


# Create your views here.
class CoinList(generics.ListCreateAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    

    # def delete(self, request, *args, **kwargs):
    #     Coin.objects.all().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CoinRetrieve(generics.ListAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    lookup_field = 'coinSymbol'
    # def get_queryset(self):
    #     coinSymbol = self.request.query_params.get('coinSymbol', None)
    #     if coinSymbol:
    #         return Coin.objects.filter(coinSymbol__icontains=coinSymbol)
    #     else:
    #         return Coin.objects.all()


class AlertsRetrieve(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class CoinList(APIView):
    serializer_class = CoinSerializer

    def get_queryset(self):
        title = 'BTC'
        alerts = Alert.objects.filter(title_icontains=title)
    # def get(self, request, format=None):
    #     title = request.query_paramter_get('title', '')

    #     if title:
    #         alerts = Alert.objects.filter(title_icontains=title)
    #     else:
    #         alerts = Alert.objects.all()
    #     serializer = AlertSerializer(alerts, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def getData(request):
#     app = Coin.objects.all()
#     serializer = CoinSerializer(app, many=True)
#     return Response(serializer.data)
