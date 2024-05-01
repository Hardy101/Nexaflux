from rest_framework import generics
from .models import Coin, Alert
from .serializers import CoinSerializer, AlertSerializer



# Create your views here.
class CoinList(generics.ListAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class AlertsRetrieve(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer