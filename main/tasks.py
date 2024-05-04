from celery import shared_task
import requests
from datetime import datetime
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# VARIABLES
ENDPOINT = 'https://api.npoint.io/fc1045cc362997a2adb3'

@shared_task
def check_alerts():
    response = requests.get(ENDPOINT)
    alert_list = response.json()

    current_time = datetime.now()
    for alert_data in alert_list:
        valid_until = datetime.strptime(alert_data['validuntil'], '%Y-%m-%d %H:%M:%S')
        if current_time < valid_until:
            dummy.appy_async()

@shared_task
def dummy():
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.create(
        interval=interval,
        Name='dummy1',
        task='main.tasks.dummy',

    )