import numpy as np
import discord
import os

ini_word = 'A-'
alice_dict = {'hello': 'Hello!', 'baka': 'You are real baka and ⑨!'}

async def Alice_talking(message):

    if message.content.startswith(ini_word+'hello') or message.content.startswith(ini_word+'Hello'):
        await message.channel.send(alice_dict['hello'])
    elif message.content.startswith(ini_word+'baka') or message.content.startswith(ini_word+'Baka'):
        await message.channel.send('You are real baka and ⑨!')