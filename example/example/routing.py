from channels.routing import route
from landing.consumers import ws_add, ws_message, ws_disconnect, hello_10, hello_30

channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    route('background-10', hello_10),
    route('background-30', hello_30),
]
