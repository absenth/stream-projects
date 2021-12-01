import discord
import os
import random
import asyncio
import websockets
import json
import tauclient
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


async def run_all():
    discord_client = client.start(user_token)
    notification_channel = await client.fetch_channel(707230298714275872)
    tauclient_client = tauclient.listen(notification_channel)
    await asyncio.gather(discord_client, tauclient_client)

asyncio.run(run_all()) # no need to explicitly get the event loop past 3.7 or 3.8

# Bot "goes online" when the script is run
# Bot does not respond to keywords
# Bot does not respond to `Stream-online` events
# https://stackoverflow.com/questions/66197394/client-get-channelid-returning-none-on-a-channel-that-exists/66197697#66197697
