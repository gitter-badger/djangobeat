from django.apps import AppConfig
from scheduler import Scheduler


class DjangoBeatConfig(AppConfig):
    name = 'djangobeat'
    verbose_name = 'Django Beat'

    def ready(self):
        periodictask = self.get_model('PeriodicTask')
        all_task = periodictask.objects.all()
        for task in all_task:
            sche = Scheduler(
                schedule=task.schedule, channel_name=task.channel_name)
            sche.agent()
