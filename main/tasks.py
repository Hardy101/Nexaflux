from celery import shared_task
import requests
from datetime import datetime
from .models import Alert

# //VARIABLES
ENDPOINT = 'http://127.0.0.1:8000/api/alerts/'


@shared_task
def check_alerts():
    response = requests.get('your_api_endpoint_here')
    alert_list = response.json()

    # Process the fetched data
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    for alert_data in alert_list:
        valid_until = datetime.strptime(alert_data['validuntil'], '%Y-%m-%d %H:%M:%S')
        if current_time < valid_until:
            # Schedule a task for each due alert
            'Hello world!'.apply_async()