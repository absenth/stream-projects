import websockets
import asyncio
import os
import json
from pprint import pprint

async def listen():
    url = 'ws://192.168.1.204:8000/ws/twitch-events/'
    tau_token = os.getenv('TAU_TOKEN')
    json_data = '{ \"token\": \"%s\" }'%tau_token

    async with websockets.connect(url) as ws:
        await ws.send(json_data)
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            event_type = data['event_type']
            streamer = data['event_data']['broadcaster_user_name']
            if event_type == 'stream-online':
                print(f'{streamer} has just gone live.  Check them out at https://twitch.tv/{streamer}')


asyncio.get_event_loop().run_until_complete(listen())
