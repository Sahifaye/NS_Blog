from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from blog.forecastApi import update_forecast

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_forecast, 'interval', minutes=30)
    scheduler.start()