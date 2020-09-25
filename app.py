from bot.bot import client
from bot import discord_config

if __name__ == "__main__":
    """ Running the file from a single source which is at the top most parent level."""
    client.run(discord_config['token'])
