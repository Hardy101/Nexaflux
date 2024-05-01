from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Coin, Alert
from .serializers import CoinSerializer, AlertSerializer


# Create your views here.
class CoinCreate(generics.ListCreateAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer

    def delete(self, request, *args, **kwargs):
        Coin.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CoinRetrieve(generics.RetrieveAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    lookup_field = 'coinSymbol'


class AlertsRetrieve(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertList(APIView):
    def get(self, request, format=None):
        title = request.query_paramter_get('title', '')

        if title:
            alerts = Alert.objects.filter(title_icontains=title)
        else:
            alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def getData(request):
#     app = Coin.objects.all()
#     serializer = CoinSerializer(app, many=True)
#     return Response(serializer.data)
