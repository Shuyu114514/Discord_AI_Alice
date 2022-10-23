import numpy as np
import discord
import os

ini_word = 'a-'
alice_dict = {'hello': 'Hello!', 'Hello': 'Hello!',
              'baka': 'You are real baka and ⑨!', 'Baka': 'You are real baka and ⑨!',
              'I love you': 'I love you, too.'
              }


async def alice_talking(message):
    for i in alice_dict:
        if message.content.startswith(ini_word + i):
            await message.channel.send(alice_dict[i])
