# In consumers.py
from channels import Group


# Connected to websocket.connect
def ws_add(message):
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


# consumers.py
def hello_10(message):
    print("Hello, Channels!, 10")  # long running task or printing 10


# consumers.py
def hello_30(message):
    print("Hello, Channels!, 30")  # long running task or printing 10
