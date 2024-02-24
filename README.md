# Discord_Event_Chat
A simple chatbot where when a discord event is created it creates a private thread under a channel.
When a user is interested in the event, they get added to the thread. when un interested, they get removed.
On deletion or completion of the event, the thread gets deleted.

.env is required that contains the following:
DISCORD_TOKEN={BotToken}
EVENT_CHANNEL_ID={ChannelId under which threads will be created}