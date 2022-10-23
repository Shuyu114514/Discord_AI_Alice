import numpy as np
import discord
import os
import requests
import json

# Import other files from this project:
import talking
import games

# Please create a txt file named Alice_Token and write done the token at the first line
f = open('Alice_Token.txt', 'r')
lines = f.readlines()
TOKEN = lines[0]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Your lovely maid Alice({0.user}) is here.'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await talking.alice_talking(message)
    await games.random_num(message)

client.run(TOKEN)
