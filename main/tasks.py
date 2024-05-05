from django.conf import settings
import requests
from datetime import datetime
from alerts_and_data.models import Alert

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
    if still_valid:
        for item in still_valid():
            id = item['id']
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
            alert_instance = Alert.objects.get(pk=id)
            alert_instance.status = 'fulfilled'
            alert_instance.save()
            # if int(float(target)):
            #     entries.append(item)
    else:
        print('Sorry, Nothing here...')
    # print(entries)

