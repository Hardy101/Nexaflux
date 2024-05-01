from django.core.management.base import BaseCommand
from alerts_and_data.models import Coin  # Replace 'myapp' with the name of your Django app
import json

class Command(BaseCommand):
    help = 'Load coins from a text file into the database'

    def add_arguments(self, parser):
        parser.add_argument("coinlist.txt", type=str, help='The path to the text file')

    def handle(self, *args, **kwargs):
        filename = kwargs['coinlist.txt']
        with open(filename, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                    try:
                        coin_data = json.loads(line)
                    except json.JSONDecodeError as e:
                        error_info = {
                            'error': str(e),
                            'line_number': line_number,
                            'error_position': e.pos,
                            'error_line': line.strip()
                        }
                        self.stderr.write(f"Error decoding JSON on line {line_number}: {error_info}")
                        continue
                    try:
                        Coin.objects.create(coinName=coin_data['coinName'], coinSymbol=coin_data['coinSymbol'])
                    except KeyError as e:
                        self.stderr.write(f"Error creating Coin object on line {line_number}: {e}")
                        continue
        self.stdout.write(self.style.SUCCESS('Coins loaded successfully'))

