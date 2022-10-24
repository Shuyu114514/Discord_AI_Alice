import numpy as np
import discord
import os
import random
import re

ini_word = 'a-'
message_send = ''
reg_ndn = 'a[-][1-9]d+[0-9]'


async def random_num(message):
    if message.content == (ini_word + 'random number'):
        message_send = 'My master, I generated a random number between 0 and 1 for you: %f' % random.random()
        await message.channel.send(message_send)
	
	if re.match(message.content, reg_ndn):
		result = 0
		
		word_ndn = message.content[2:]
		lst_ndn = word_ndn.split('d')
		num_dice = int(lst_ndn[0])
		dice_range = int(lst_ndn[1])
		
		if dice_range == 0:
			message_send = 'My master, the number on a die should be at least 1!"
			await message.channel.send(message_send)
			
		for i in range(num_dice):
			temp = random.randint(1,dice_range)
			result += temp
			
		message_send = 'My master, the die is cast and the result is: %f' % result
