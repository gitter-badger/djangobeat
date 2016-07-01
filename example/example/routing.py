from channels.routing import route
from .consumers import hello_10

channel_routing = [
    route('background-10', hello_10),
]
