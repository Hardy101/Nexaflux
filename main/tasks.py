import requests
from datetime import datetime
from django.utils import timezone
from alerts_and_data.models import Alert

ENDPOINT = 'https://api.npoint.io/fc1045cc362997a2adb3'
PRICE_ENDPOINT = 'https://min-api.cryptocompare.com/data/price'

def getvaliddata():
    response = requests.get(ENDPOINT)
    data = response.json()

    current_time = timezone.now()

    due_entries = []

    for item in data:
        timestamp_str = item['validuntil']
        status = item['status']
        timestamp = datetime.fromisoformat(timestamp_str)

        # if timestamp > current_time and status == 'active':
        if timestamp and status == 'active':
            due_entries.append(item)
             
    return due_entries

def send_sms():
    for entry in getvaliddata():
        print(entry['status'], entry['coin'])

def getcoinprice(parameters):
    data = requests.get(PRICE_ENDPOINT, params=parameters).json()
    return data['USDT']


def updatecoinstatus(id):
    alert_instance = Alert.objects.get(pk=id)
    alert_instance.status = 'fulfilled'
    alert_instance.save()

def check_price():
    for item in getvaliddata():
        id = item['id'] 
        targetprice = item['target']
        coin = item['coin']
        recipient = item['recipient']
        params = {'fsym': coin, 'tsyms': 'USDT'}

        # Fetching price data
        # price = getcoinprice(parameters=params)
        
        # Printing message
        print(f'congrats🎉 dear {recipient}, Your target of {targetprice}USDT has been met,')

        # Updating status to 'fulfilled'
        updatecoinstatus(id=id)

