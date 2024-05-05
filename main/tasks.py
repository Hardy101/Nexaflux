from django.conf import settings
import requests
import json
import random
from datetime import datetime


postcodes = [
	"SW1A 1AA",
	"PE35 6EB", 
	"CV34 6AH",
	"EH1 2NG"
]

def schedule_api():

	postcode = postcodes[random.randint(0, 3)]

	full_url = f"https://api.postcodes.io/postcodes/{postcode}"
			
	r = requests.get(full_url)
	if r.status_code == 200:

		result = r.json()["result"]

		lat = result["latitude"]
		lng = result["longitude"]

		print(f'Latitude: {lat}, Longitude: {lng}')

		#77779


def check_api_endpoint():
    pass


def still_valid():
    response = requests.get('https://api.npoint.io/fc1045cc362997a2adb3')
    data = response.json()

    due_entries = []

    for item in data:
        timestamp_str = item['validuntil']
        timestamp = datetime.fromisoformat(timestamp_str)

        if datetime.now():
              due_entries.append(item)
    return due_entries

def send_sms():
      for entry in still_valid():
            print(entry['status'], entry['coin'])