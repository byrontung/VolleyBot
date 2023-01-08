# This example requires the 'message_content' intent.

"""
Taken from the docs:
https://discordpy.readthedocs.io/en/latest/intro.html#installing
"""

#dbgVA7G-zg45aDYmKeuj38v34rjd-q--
#https://discord.com/api/oauth2/authorize?client_id=1061503173157728367&permissions=1634235579456&scope=bot

# import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')

# intents = discord.Intents.default()
# intents.message_content = True

# client = MyClient(intents=intents)
# client.run('my token goes here')

import bot

if __name__ == '__main__':
	bot.run_discord_bot()