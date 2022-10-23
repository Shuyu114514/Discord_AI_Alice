import numpy as np
import discord
import os
import talking

TOKEN = 'MTAzMjg3NTQxOTIxMDM1ODc4NA.Gh6heV.pvbaztnuyA4R0G0CgHY8hjE_28BCUPi1ONT-10'

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
