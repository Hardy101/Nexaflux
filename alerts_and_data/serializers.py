from rest_framework import serializers
from .models import Coin, Alert

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'coinName','coinSymbol']

  
class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        # fields = ['id', 'coin','target_type', 'target', 'date_created']
        fields = '__all__'