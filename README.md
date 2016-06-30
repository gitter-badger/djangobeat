# djangobeat

Periodic Tasks for Django channels


### Installation

	pip install -U DjangoBeat
	
### Settings

    INSTALLED_APPS += ['djangobeat']

	CHANNEL_LAYERS = {
	    "default": {
	        "BACKEND": "asgiref.inmemory.ChannelLayer",
	        "ROUTING": "example.routing.channel_routing",
	        "BEAT": "example.beatconfig.DJANGOBEAT_SCHEDULE" # your beat
	    },
	}

	    
	    
### Beat Config ###
you should create beatconfig.py in your project root

	DJANGOBEAT_SCHEDULE = {
	    'add-every-30-seconds': {
	        'schedule': 5,
	        'channel': 'background-hello'
	    },
	}
