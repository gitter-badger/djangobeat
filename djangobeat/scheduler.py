import time
# import datetime
import threading
from channels import Channel


def scheduler(schedule, channel_name):
    while True:
        Channel(channel_name).send({})
        time.sleep(schedule)


def agent(schedule, channel_name):
    timerThread = threading.Thread(
        target=scheduler, args=[schedule, channel_name, ])
    timerThread.daemon = True
    timerThread.start()
