import discord
import responses

async def send_message(message, user_message, is_private):
	try:
		response = responses.handleResponse(user_message)
		await message.author.send(response) if is_private else message.channel.send(response)
	except Exception as e:
		print(e)


def run_discord_bot():
	#dbgVA7G-zg45aDYmKeuj38v34rjd-q--
#https://discord.com/api/oauth2/authorize?client_id=1061503173157728367&permissions=1634235579456&scope=bot

	TOKEN = "https://discord.com/api/oauth2/authorize?client_id=1061503173157728367&permissions=1634235579456&scope=bot"
	client = discord.Client(discord.Intents.default())

	@client.event
	async def on_ready():
		print(f"{client.user} is now running!")

	client.run(TOKEN)