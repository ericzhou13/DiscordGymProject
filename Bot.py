import time
import discord #for discord
from discord.ext import commands #gets commands for discord bot
import logging #for logging information to cmd
from pathlib import Path #for paths




token = "MTA4NDY1MjY3OTMyMzcxMzU4Nw.Gww3iS.W_Fu1O6zggE-zvCuGTyh3zH3x_SQQ5Zbqr3dsw"
client = discord.Client()#creates and instance of the client that connects to discord



@client.event
async def on_ready():
	print("We have logged in")
	
@client.event
async def on_message(message):
	id = client.get_guild(1084655332703350844)
	if message.content.startswith("!send") != -1:
		await message.channel.send("Test")

client.run(token)
	