from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import check_price

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(check_price, 'interval', seconds=5)
	scheduler.start()
