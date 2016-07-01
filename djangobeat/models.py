from __future__ import unicode_literals
from django.db import models
# for signal import
from django.db.models.signals import post_save
from django.dispatch import receiver
# schedular config
from scheduler import agent


class PeriodicTask(models.Model):
    task_name = models.CharField(max_length=220)
    channel_name = models.CharField(max_length=220)
    schedule = models.DurationField()

    def __str__(self):
        return "{}".format(self.task_name)


@receiver(post_save, sender=PeriodicTask)
def post_handler(sender, **kwargs):
    instance = kwargs['instance']
    agent(instance.schedule.total_seconds(), instance.channel_name)
