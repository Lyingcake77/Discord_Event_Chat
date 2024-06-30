# Discord_Event_Chat
A simple chatbot where when a discord event is created it creates a private thread under a channel.
When a user is interested in the event, they get added to the thread. when un interested, they get removed.
On deletion or completion of the event, the thread gets deleted.

.env is required that contains the following:
DISCORD_TOKEN={BotToken}
EVENT_CHANNEL_ID={ChannelId under which threads will be created}
ROLE_MANAGER_MESSAGE_ID={Message that will be monitered for reactions to assign roles}

TODO:
Guild ID to fix a bot updating across multiple servers
github actions to deploy to server
get rid of docker copy.. and ignore .env files

fix on event create code with the Next() issue

make bot respond to commands so that  I can set it up with custom Id's
add a kill switch