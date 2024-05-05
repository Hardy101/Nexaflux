from django.conf import settings
import requests
from datetime import datetime


def still_valid():
    response = requests.get('https://api.npoint.io/fc1045cc362997a2adb3')
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