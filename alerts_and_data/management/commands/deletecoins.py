from django.core.management.base import BaseCommand
from alerts_and_data.models import Coin

class Command(BaseCommand):
    help = 'Clear all data from the Coin model'

    def handle(self, *args, **kwargs):
        Coin.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All data cleared from the Coin model'))
