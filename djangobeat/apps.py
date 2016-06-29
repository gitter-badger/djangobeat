from django.apps import AppConfig
# beat import
from djangobeat import beating


class DjangoBeatConfig(AppConfig):
    name = 'djangobeat'
    verbose_name = 'Django Beat'

    def ready(self):
        instance = beating.Beater()
        instance.main()
