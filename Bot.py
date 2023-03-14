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
	#!add workout to dictionary
	with open("workouts.json", "r") as f:
		data = json.load(f)
		if(args[0] in data.keys()):
			await ctx.send("already logged")
		else:
			data[args[0]] = int(args[1])
			with open("workouts.json", "w") as f:
				json.dump(data, f)

@client.command()
async def printWorkouts(ctx):
	with open("workouts.json", "r") as f:
		data = json.load(f)
		for key in data.keys():
			await ctx.send(str(key) + " : " + str(data[key]))



@client.command()
async def test(ctx):
	await ctx.send(ctx.author.id)


@client.command()
async def end(ctx):
	exit()

print(token)
client.run(token)

