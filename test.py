# test.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)

#on event creation, create new channel/ thread
# when event is set to canceled or compelted, delete channel/ thread

#when user is "Interested" in event, add user to channel/ thread
#when user is disinterested in event, remove user from channel/ thread
