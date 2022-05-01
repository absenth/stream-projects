import os
import urllib
import requests
import json
from pprint import pprint

base_url = os.getenv('NGROK_TAU_URL')
tau_token = os.getenv('TAU_TOKEN')

query_path = 'api/v1/twitch-events'
#query_path = 'api/v1/heartbeat'
#query_path = f"api/v1/twitch/helix-endpoints/"

headers = {
        "Authorization": f"Token {tau_token}",
}

def main():
    response = requests.get(f"{base_url}/{query_path}", headers=headers)
    x = response.json()
    stream_online = x["results"][0]["event_type"]
    if stream_online == 'stream-online':
        pprint(stream_online)


if __name__ == '__main__':
    main()
