# simple discord bot template

import discord
from discord.ext import commands
import requests
import os # cleans console

os.system("cls") # cleans console

token = "x" # bot token here!
client_secret = "/" # leave blank if u are using token
prefix = "!" # prefix

status = discord.Status.online # status
activity = discord.Activity # go to line 25 if u want to change the status

intents = discord.Intents.all()
client = commands.Bot(command_prefix= prefix, intents = intents)
client.remove_command('help') # removes help command so u can make a custom one if u want
status = status
activity = activity

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('status')) # if you want to change the status, change it here

print("hi >.<")

# commands

# to add more commands, simply copy and paste line 30,31,32 and change "hi" to the command and "answer" to the bots answer!

# important: START ADDING COMMANDS HERE, NOT EARLIER!

@client.command()
async def hi(ctx): # command
    await ctx.send("Answer")

@client.command()
async def secondCommandExample(ctx): # how you should copy and paste it example
    await ctx.send("Answer")

# dont add more commands after line 45!
print("for more help dm anhediona on discord")

client.run(token)

# make sure you have discord, requests and os installed! to do that simply open cmd and type "pip install os", "pip install discord" and "pip install requests"