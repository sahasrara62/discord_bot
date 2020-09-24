from bot.bot import client
from bot import discord_config

if __name__ =="__main__":
    client.run(discord_config['token'])
