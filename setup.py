from setuptools import find_packages, setup
from djangobeat import __version__

setup(
    name='djangobeat',
    version=__version__,
    url='http://github.com/rajasimon/djangobeat',
    author='Raja Simon',
    author_email='rajasimon@icloud.com',
    description='Periodic Tasks for Django Channels',
    packages=find_packages(exclude=("example",)),
    install_requires=[
        'Django', 'Channels', 'asgiref', 'daphne',
    ]
)
