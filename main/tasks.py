from celery import shared_task
import requests
from datetime import datetime
from .models import Alert

# VARIABLES
ENDPOINT = 'https://api.npoint.io/fc1045cc362997a2adb3'

@shared_task
def hello_world():
    print('Hello World')

@shared_task
def check_alerts():
    response = requests.get(ENDPOINT)
    alert_list = response.json()

    # Process the fetched data
    current_time = datetime.now()
    for alert_data in alert_list:
        valid_until = datetime.strptime(alert_data['validuntil'], '%Y-%m-%d %H:%M:%S')
        if current_time < valid_until:
            # Schedule a task for each due alert
            hello_world.CELE()
