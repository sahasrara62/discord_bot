import discord
from bot import  search_result, get_recent_query

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('hi'):
            msg = 'hey {0.author.mention} '.format(message)
            await message.channel.send(msg)

        if message.content.startswith("!google"):
            query = message.content.lstrip("!google").strip()
            if not query:
                await message.channel.send("Enter the search item")
            await message.channel.send("please wait, loading the google results : ")
            for res in search_result(query, message.author.id):
                await message.channel.send(res)

        if message.content.startswith("!recent"):
            query = message.content.lstrip("!recent").strip()
            if not query:
                res = list(get_recent_query(str(message.author.id)))
                if not res:
                    await message.channel.send("No searches made by so far")
                else:
                    await message.channel.send("your recent searches")
                    for val in res:
                        await message.channel.send(val)

            else:
                result = list(get_recent_query(str(message.author.id), msg=query))

                if len(result)>0:
                    for res in result:
                        await message.channel.send(res)
                else:
                    await message.channel.send('not recent searches related to query {}'.format(query))

client = MyClient()
