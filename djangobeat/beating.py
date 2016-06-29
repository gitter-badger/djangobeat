import importlib
from django.utils import six
from django.conf import settings
from djangobeat import scheduler


class Beater(object):
    """
    Beater is the main object has the extract the information from configs
    """

    def config(self):
        # extract CHANNEL_LAYERS
        return getattr(settings, "CHANNEL_LAYERS", {})

    def get_beat_config(self):
        return self.config()['default']['BEAT']

    def get_tasks(self):
        # GET the TASK defined there
        beat_config = self.get_beat_config()
        if isinstance(beat_config, six.string_types):
            module_name, variable_name = beat_config.rsplit(".", 1)
            beat = getattr(importlib.import_module(module_name), variable_name)
            return beat

    def main(self):
        all_task = self.get_tasks()
        for task in self.get_tasks():
            which_channel = all_task[task]['channel']
            schedule = all_task[task]['schedule']
            schedular_instance = scheduler.Scheduler()
            schedular_instance.run_task(schedule, which_channel)
