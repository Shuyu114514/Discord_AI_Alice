import numpy as np
import discord
import os
import random

ini_word = 'a-'
message_send = ''


async def random_num(message):
    # if message.content.startswith(ini_word + 'random number'):
    if message.content == (ini_word + 'random number'):
        message_send = 'My master, I generated a random number between 0 and 1 for you: %f' % random.random()
        await message.channel.send(message_send)
