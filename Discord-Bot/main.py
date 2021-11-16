import discord
import os
import random

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

client.run(user_token)
