import websockets
import asyncio
import os
import json
from pprint import pprint

async def listen():
    url = "ws://192.168.1.204:8000/ws/twitch-events/"
    tau_token = os.getenv("TAU_TOKEN")
    json_data = '{ \"token\": \"%s\" }'%tau_token

    async with websockets.connect(url) as ws:
        await ws.send(json_data)
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            event_type = data['event_type']
            streamer = data['event_data']["broadcaster_user_name"]
            print(f"{streamer} has just {event_type}")


asyncio.get_event_loop().run_until_complete(listen())


''' Full MSG output example

{
    "id": "73365ffc-0bbb-425f-8590-43faf1c79385",
    "event_id": ' '"Z3M6Rdp7YkTR3l1EzKhwPNLCtailbcznj9nvaFD4jMc=",
    "event_type": ' '"channel-update",
    "event_source": "EventSub",
    "event_data": '
      '{
        "broadcaster_user_id": "425930108",
        "broadcaster_user_login": "absenth762", ' '
        "broadcaster_user_name": "absenth762",
        "title": "#100DaysOfCode - Day 15 - ' 'parsing message as JSON broken.\\n\\n",
        "language": "en",
        "category_id": ' '"1469308723",
        "category_name": "Software and Game Development",
        "is_mature": ' 'false
      },
    "created": "2021-11-28T22:59:01+0000",
    "origin": "twitch"
}

'''
