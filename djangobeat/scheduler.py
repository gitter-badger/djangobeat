import sched
import time
from channels import Channel
from threading import Thread


class Scheduler(object):
    """
    scheduler have the advantage of the sched and thread module. Instance will
    run the run_task command and inside the UpdateThread will repeat the
    process continuously
    """

    s = sched.scheduler(time.time, time.sleep)

    def run_task(self, schedule, which_channel):
        class UpdateThread(Thread):
            def __init__(self):
                self.stopped = False
                Thread.__init__(self)

            def run(self):
                while not self.stopped:
                    Channel(which_channel).send({})
                    time.sleep(schedule)
        try:
            myThread = UpdateThread()
            myThread.daemon = True
            myThread.start()
        except (KeyboardInterrupt, SystemExit):
            print '\n! Received keyboard interrupt, quitting threads.\n'
