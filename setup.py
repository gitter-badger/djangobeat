import os
from setuptools import find_packages, setup
from djangobeat import __version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangobeat',
    version=__version__,
    url='http://github.com/rajasimon/djangobeat',
    author='Raja Simon',
    author_email='rajasimon@icloud.com',
    description='Periodic Tasks for Django Channels',
    zip_safe=False,
    packages=find_packages(exclude=("example",)),
    include_package_data=True,
    install_requires=[
        'Django', 'Channels', 'asgiref', 'daphne',
    ]
)
