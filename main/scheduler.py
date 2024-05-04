from apscheduler.schedulers.background import BackgroundScheduler
from main.management.commands.print_hello import Command

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(Command().handle, 'interval', seconds=10)
    scheduler.start()