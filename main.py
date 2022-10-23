import numpy as np
import discord
import os
import requests
import json
from discord.ext import commands, tasks

# Import other files from this project:
import switch_Alice
import talking
import games
import other_fuctions
# import switch_Alice

# Please create a txt file named Alice_Token and write done the token at the first line
f = open('Alice_Token.txt', 'r')
lines = f.readlines()
TOKEN = lines[0]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
switch_Alice = False

@client.event
async def on_ready():
    print('Your lovely maid Alice({0.user}) is here.'.format(client))


@client.event
async def on_message(message):
    global switch_Alice

    if message.author == client.user:
        return

    if message.content == 'a-turn on':
        switch_Alice = True
        await message.channel.send('Your lovely maid Alice is here.')
    elif message.content == 'a-turn off':
        switch_Alice = False
        await message.channel.send('Your lovely maid Alice goes to rest.')

    if switch_Alice:
        await talking.alice_talking(message)
        await games.random_num(message)
        await other_fuctions.action_to_voice_chat(message)


client.run(TOKEN)
