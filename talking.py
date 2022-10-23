import numpy as np
import discord
import os
import random

ini_word = 'a-'
alice_dict = {'hello': 'Hello!', 'Hello': 'Hello!',
              'baka': 'You are the real baka and ⑨!', 'Baka': 'You are the real baka and ⑨!',
              'I love you': 'I love you, too.',
              'Alice': 'Yes?', 'alice': 'Yes?', '爱丽丝': '怎么啦？'
              }
random_dict = [[['pat', 'Pat', 'hug', 'Hug'], ['Pat you~', '(´･ω･)ﾉ(._.`)', 'Hug you~']],
               [['lick', 'Lick', 'prpr'], ['Hentai!', 'Lick~', 'prprpr~']],
               [['sex', 'Sex'], ['Hentai!', 'no!', 'If you want...My master']]
               ]
message_send = ''


async def alice_talking(message):
    for i in alice_dict:
        if message.content == (ini_word + i):  # whole sentence priority
            await message.channel.send(alice_dict[i])
            return
        elif message.content.startswith(ini_word + i):
            await message.channel.send(alice_dict[i])
            return

    for i in random_dict:
        for j in i[0]:
            if message.content == (ini_word + j):
                await message.channel.send(random.choice(i[1]))
                return
            elif message.content.startswith(ini_word + j):
                await message.channel.send(random.choice(i[1]))
                return
