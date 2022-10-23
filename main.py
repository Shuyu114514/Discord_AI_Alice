import numpy as np
import discord
import os
import talking

# Please create a txt file named Alice_Token and write the token at the first line
f = open('Alice_Token.txt', 'r')
lines = f.readlines()
TOKEN = lines[0]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await talking.alice_talking(message)


client.run(TOKEN)
