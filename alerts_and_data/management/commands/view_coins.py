from django.core.management.base import BaseCommand
from alerts_and_data.models import Coin

class Command(BaseCommand):
    help = 'Print all data from the Coin model'

    def handle(self, *args, **kwargs):
        coins = Coin.objects.all()
        for coin in coins:
            self.stdout.write(self.style.SUCCESS(f"Id: {coin.id},Name: {coin.coinName}, Symbol: {coin.coinSymbol}"))