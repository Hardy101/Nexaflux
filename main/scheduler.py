from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import schedule_api, check_api_endpoint, still_valid, send_sms

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(send_sms, 'interval', seconds=5)
	scheduler.start()