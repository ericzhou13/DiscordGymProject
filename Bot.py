import time
import discord #for discord
from discord.ext import commands #gets commands for discord bot
import logging #for logging information to cmd
from pathlib import Path #for paths
import json


token = ""
with open("token.txt", "r") as f:
	token = f.readline()



client = discord.Client()#creates and instance of the client that connects to discord

@client.event
async def on_ready():
	print("We have logged in")
	
@client.event
async def on_message(message):
	if message.content.startswith("!send") != -1:
		await message.channel.send("Test")

client.run(token)
