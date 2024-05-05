from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import still_valid, send_sms, check_price

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(check_price, 'interval', seconds=5)
	scheduler.start()