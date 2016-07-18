# djangobeat

[![Join the chat at https://gitter.im/rajasimon/djangobeat](https://badges.gitter.im/rajasimon/djangobeat.svg)](https://gitter.im/rajasimon/djangobeat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Periodic Tasks for Django channels


### Installation

    pip install -U DjangoBeat

It's is important that you have to run --noreload option otherwise it will executed twice

    
### Settings

    INSTALLED_APPS += ['djangobeat']
    
### How to use

    $ python manage.py shell
    >>> from djangobeat.models import PeriodicTask
    >>> PeriodicTask.objects.create(
        task_name="hello",
        channel_name="print-hello",
        schedule=timedelta(seconds=20)
    )