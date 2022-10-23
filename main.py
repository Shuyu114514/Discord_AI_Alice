import numpy as np
import discord
import os
import talking

#TOKEN = 'MTAzMjg3NTQxOTIxMDM1ODc4NA.GED51S.S7sqhpuWDHbMLMRB84i-jSFGWszKOnMs3HUhrs'
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
    await talking.Alice_talking(message)


client.run('MTAzMjg3NTQxOTIxMDM1ODc4NA.GED51S.S7sqhpuWDHbMLMRB84i-jSFGWszKOnMs3HUhrs')
