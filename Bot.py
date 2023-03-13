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



client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
	print("We have logged in")

@client.command()
async def add(ctx, *args):
	#!add workout reps weight 
	json_string = '''
		{
			{ctx.author.id}: [
				{date}: [
					{exercise}:{
						name: 
						weight:
						reps:
						sets:
					}
				]
				{date}
				{date}
			]
		}
	
	'''
@client.command()
async def test(ctx):
	await ctx.send(ctx.author.id)


@client.command()
async def end(ctx):
	exit()

print(token)
client.run(token)

