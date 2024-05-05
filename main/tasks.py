from django.conf import settings
import requests
from datetime import datetime

ENDPOINT = 'https://api.npoint.io/fc1045cc362997a2adb3'
PRICE_ENDPOINT = 'https://min-api.cryptocompare.com/data/price'

def still_valid():
    response = requests.get(ENDPOINT)
    data = response.json()

    due_entries = []

    for item in data:
        timestamp_str = item['validuntil']
        status = item['status']
        timestamp = datetime.fromisoformat(timestamp_str)

        if datetime.now() and status == 'active':
              due_entries.append(item)
    return due_entries

def send_sms():
      for entry in still_valid():
            print(entry['status'], entry['coin'])


def check_price():
    entries = []
    for item in still_valid():
        target = item['target']
        coin = item['coin']
        recipient = item['recipient']
        params = {
         'fsym': coin,
         'tsyms': 'USDT'
        }
        # data = requests.get(PRICE_ENDPOINT, params=params).json()
        # price = data['USDT']
        print(f'congrats🎉 dear {recipient}, Your target of {target}USDT has been met,')
        # if int(float(target)):
        #     entries.append(item)
    # print(entries)

