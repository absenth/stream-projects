import websockets
import asyncio
import os
import json
from pprint import pprint

async def listen(channel):
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
                channel.send(f'{streamer} has just gone live.  Check them out at https://twitch.tv/{streamer}')

''' I don't know if this script/function knows how to send.
see the `error` file in this folder for an example traceback

That should work, but you'll probably need "await channel.send(...)"; however,
the error means it is trying to do None.send, and that None comes from the
client.get_channel not finding the channel according to the doc
'''
