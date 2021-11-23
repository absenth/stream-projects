import urllib
import requests
import json
import pprint

url = 'https://tmi.twitch.tv/group/user/absenth762/chatters'
chatters = requests.get(url).json()['chatters']
viewers = chatters["viewers"]

for viewer in viewers:
    if viewer == 'alltow':
        print("Alltow is present")

