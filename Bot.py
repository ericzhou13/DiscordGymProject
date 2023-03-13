import time
import discord #for discord
from discord.ext import commands #gets commands for discord bot
import logging #for logging information to cmd
from pathlib import Path #for paths
import json
import os

token = ""
with open("token.txt", "r") as f:
	token = f.readline().strip()


client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
	print("We have logged in")
	
@client.event
async def on_message(message):
	if message.content.find("!hello") != -1:
		await message.channel.send("Hi")
	
	if message.content.find("!end") != -1:
		exit()

print(token)
client.run(token)

