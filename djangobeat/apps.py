import logging
from django.apps import AppConfig
from scheduler import Scheduler


class DjangoBeatConfig(AppConfig):
    name = 'djangobeat'
    verbose_name = 'Django Beat'

    def ready(self):
        periodictask = self.get_model('PeriodicTask')
        try:
            all_task = periodictask.objects.all()
            for task in all_task:
                sche = Scheduler(
                    schedule=task.schedule, channel_name=task.channel_name)
                sche.agent()
        except:
            logger = logging.getLogger('django')
            logger.error(
                'Currently Djangobeat support only with Database level beat' +
                'config, please make sure your DB setup correctly!')
            pass
