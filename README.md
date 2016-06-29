# djangobeat

Periodic Tasks for Django channels

### Installation: ###


	pip install -U djangobeat


### How to setup: ###

	# In settings.py
	CHANNEL_LAYERS = {
	    "default": {
	        "BACKEND": "asgiref.inmemory.ChannelLayer",
	        "ROUTING": "example.routing.channel_routing",
	        "BEAT": "example.beatconfig.DJANGOBEAT_SCHEDULE" # your beat
	    },
	}


	# In routing.py
	channel_routing = [
	    route('background-hello', hello), # your beat
	]

	# consumers.py
	def hello(message):
	    print("Hello, Channels!")  # your beat
