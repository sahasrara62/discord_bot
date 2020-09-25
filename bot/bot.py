import discord
from bot import search_result, get_recent_query


class MyClient(discord.Client):

    async def on_ready(self):
        """
        showing message on console when the server start
        :return:
        """
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        # event listener, where sending message is a event

        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        print('Message from {0.author}: {0.content}'.format(message))

        # checking the conditions, with which the user input starts
        # if user input is hi, return hey
        if message.content.startswith('hi'):
            msg = 'hey {0.author.mention} '.format(message)
            await message.channel.send(msg)

        # if user input is !google query, provide result
        if message.content.startswith("!google"):

            # getting query from the input
            query = message.content.lstrip("!google").strip()

            if not query:
                await message.channel.send("Enter the search item")

            await message.channel.send("please wait, loading the google results : ")

            #  returning all the search result one by one
            for res in search_result(query, message.author.id):
                await message.channel.send(res)

        # identify, user want to see the result from his previous search history

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

                if len(result) > 0:
                    for res in result:
                        await message.channel.send(res)
                else:
                    await message.channel.send('not recent searches related to query {}'.format(query))


client = MyClient()
