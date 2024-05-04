from celery import shared_task
import requests
from datetime import datetime
import requests


@shared_task
def print_hello_world(timestamp):
    if timestamp <= datetime.now():
        print('hello-world')


@shared_task
def check_api_endpoint():
    response = requests.get('https://api.npoint.io/fc1045cc362997a2adb3')
    data = response.json()
    for item in data:
        timestamp = item['timestamp']
        print_hello_world.apply_async(args=[timestamp], eta=timestamp)

