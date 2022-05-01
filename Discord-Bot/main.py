import discord
import requests
import os
import random
import asyncio
import websockets
import json

user_token = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.lower() == 'hello':
        await message.channel.send(f'Hi {username}!')
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'See y later {username}!')
        return
    elif user_message.lower() == 'goodnight':
        await message.channel.send('Sleep is an inappropriate substitute for caffeine!')
        return


@client.event
async def announce_live():  # FIXME -- this function doesn't appear to fire
    channel = 'announcements'
    is_live = False
    while True:
        if is_live == False:
            if check_stream():
                await message.channel.send('Absenth762 is live!')
                is_live = True
                return


def check_stream(): # FIXME -- This function likely works, but I don't know for sure
    base_url = os.getenv('NGROK_TAU_URL')
    tau_token = os.getenv('TAU_TOKEN')
    query_path = 'api/v1/twitch-events'
    headers = {
            "Authorization": f"Token {tau_token}",
            }
    response = requests.get(f"{base_url}/{query_path}", headers=headers)
    x = response.json()
    stream_online = x["results"][0]["event_type"]
    if stream_online == 'stream-online':
        return True

client.run(user_token)
