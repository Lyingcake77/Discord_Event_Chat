# main.py
import os
import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
EventChannelId = os.getenv('EVENT_CHANNEL_ID')
WelcomeText = "Welcome to an automatically generated private thread. You've been added because you are interested in this event. This thread will be deleted once you are not interested in the event or once it Ends."
ReminderText = "Event has begun, please remember that this chat will be deleted once the event finishes."
# This example requires the 'message_content' intent.

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{datetime.now()}: Logged on as {self.user}!')

    # async def on_message(self, message):
    #     if message.author == client.user:
    #         return

    #     if message.content.startswith('$hello'):
    #         await message.channel.send('Hello!')
        
    ###
    # When an event is created, create a new private thread
    # and add a user to the new thread.
    ###
    async def on_scheduled_event_create(client, event):
        print(f'{datetime.now()}: {event.name} event created')
        if event.status.name == "scheduled":
            channel = client.get_channel(int(EventChannelId))
            thread = await channel.create_thread(
                name=event.name
            ) 
            
            await thread.send(WelcomeText)
            #event add user is called, but before the new thread gets returned, therefore this is done here.
            await thread.add_user(event.creator)
    ###
    # When an event is cancled, delete the thread
    ###    
    async def on_scheduled_event_delete(client, event):
        #add user to private thread
        print(f'{datetime.now()}: {event.name} event deleted')
        channel = client.get_channel(int(EventChannelId))
        thread = get_channel_thread(channel, event)
        if thread != None:
            await thread.delete()
    ###
    # When an event is updated, make a change
    # changes can include a status change to started, endewd, or a name change
    ###
    async def on_scheduled_event_update(client, before, after):
        print(f'{datetime.now()}: {before.name} event updated')
        channel = client.get_channel(int(EventChannelId))
        thread = get_channel_thread(channel, before)
        if before.status.name == 'scheduled' and after.status.name == 'active':
            print(f'event started')
            if thread != None:
                await thread.send(ReminderText)
        elif before.status.name == 'active' and after.status.name == 'completed':
            print(f'event ended')
            if thread != None:
                await thread.delete()
        if before.name != after.name:
            print(f'event renamed')
            if thread != None:
                await thread.edit(name = after.name)
            
    ###
    # when a user is interested in an event
    # they are added to the the thread
    ###
    async def on_scheduled_event_user_add(client, event, user):
        #add user to private thread
        print(f'{datetime.now()}: {event.name} event user added')
        channel = client.get_channel(int(EventChannelId))
        thread = get_channel_thread(channel, event)
        if thread != None:
            await thread.add_user(user)
    ###
    # when a user is removes their interest in an event
    # they are removed from the thread
    ###
    async def on_scheduled_event_user_remove(client, event, user):
        print(f'{datetime.now()}: {event.name} event user removed')
        
        channel = client.get_channel(int(EventChannelId))
        thread = get_channel_thread(channel, event)
        if thread != None:
            await thread.remove_user(user)
            


def get_channel_thread(channel, event):
    return next((f for f in channel.threads if ('' if f == None else f.name ) == event.name), None)
    #return thread 
    
intents = discord.Intents.all()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
