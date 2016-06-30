# djangobeat

Periodic Tasks for Django channels


### Settings & Declaration: ###

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
	    
	    
### Beat Config ###
you should create beatconfig.py in your project root

	DJANGOBEAT_SCHEDULE = {
	    'add-every-30-seconds': {
	        'schedule': 5,
	        'channel': 'background-hello'
	    },
	}

