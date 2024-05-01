from django.core.management.base import BaseCommand
from alerts_and_data.models import Coin

class Command(BaseCommand):
    help = 'Delete a specific coin from the database'

    def add_arguments(self, parser):
        parser.add_argument('coin_symbol', type=str, help='The symbol of the coin to delete')

    def handle(self, *args, **kwargs):
        coinSymbol = kwargs['coin_symbol']
        try:
            coin = Coin.objects.get(coinSymbol=coinSymbol)
            coin.delete()
            self.stdout.write(self.style.SUCCESS(f'Coin with symbol {coinSymbol} deleted successfully'))
        except Coin.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'Coin with symbol {coinSymbol} does not exist'))
