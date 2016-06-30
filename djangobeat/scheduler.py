import time
# import datetime
import threading
from channels import Channel


def scheduler(schedule, which_channel):
    while True:
        Channel(which_channel).send({})
        time.sleep(schedule)


def agent(schedule, which_channel):
    timerThread = threading.Thread(
        target=scheduler, args=[schedule, which_channel, ])
    timerThread.daemon = True
    timerThread.start()
