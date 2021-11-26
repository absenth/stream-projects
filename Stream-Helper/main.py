import os
import urllib
import requests

client_id = os.getenv('TWITCH_HELPER_CLIENT_ID')
client_secret = os.getenv('TWITCH_HELPER_CLIENT_SECRET')


'''
https://www.therelicans.com/wyhaines/twitch-eventsub-the-direct-approach-to-getting-started-with-it-3pia
we want to use eventsub, it's the future of Twitch API interactions.
https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types#stream-online
will require a real URL & SSL key for Twitch to POST events once subscribed.
https://www.youtube.com/watch?v=JTE77t0j4Fc&t=252s - example tutorial maybe?
https://github.com/bsquidwrd/ubiquitous-adventure
'''
