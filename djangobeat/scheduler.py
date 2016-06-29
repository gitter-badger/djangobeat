import sched
import time
from channels import Channel
from threading import Thread


class Scheduler(object):

    s = sched.scheduler(time.time, time.sleep)

    def run_task(self, schedule, which_channel):
        # Timer(schedule, self.push_command, [schedule, which_channel, ]).start()
        # self.s.enter(schedule, 1, self.push_command, [which_channel])
        # self.s.run()

        #  new here
        class UpdateThread(Thread):
            def __init__(self):
                self.stopped = False
                Thread.__init__(self) # Call the super construcor (Thread's one)

            def run(self):
                while not self.stopped:
                    Channel(which_channel).send({})
                    # self.push_command(schedule, which_channel)
                    time.sleep(schedule)

        myThread = UpdateThread()
        myThread.start()


    # def push_command(self, schedule, which_channel):
    #     print which_channel
    #     Channel(which_channel).send({})
