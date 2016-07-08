import time
import threading
from channels import Channel


class Scheduler(object):

    def __init__(self, schedule, channel_name):
        self.schedule = schedule
        self.channel_name = channel_name

    def trigger(self):
        while True:
            Channel(self.channel_name).send({})
            time.sleep(self.schedule.total_seconds())

    def agent(self):
        # old code ref, args=[self.schedule, self.channel_name, ]
        timerThread = threading.Thread(
            target=self.trigger)
        timerThread.daemon = True
        timerThread.start()
