import os
import urllib
import requests
import json
from pprint import pprint

base_url = os.getenv('NGROK_TAU_URL')
query_path = 'api/v1/twitch-events'
#query_path = 'api/v1/heartbeat'
tau_token = os.getenv('TAU_TOKEN')

headers = {
        "Authorization": f"Token {tau_token}",
}

def main():
    response = requests.get(f"{base_url}/{query_path}", headers=headers)
    x = response.json()
    stream_online = x["results"][0]["event_type"]
    pprint(stream_online)

if __name__ == '__main__':
    main()
