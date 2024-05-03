# tasks.py
from celery import shared_task
from alerts_and_data.models import Alert
import datetime

@shared_task
def process_data(data):
    # Perform specific function with the data
    print("Processing data:", data)