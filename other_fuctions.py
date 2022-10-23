import numpy as np
import discord
import os
import random
from discord.ext import commands, tasks
# import PyNaCl

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

ini_word = 'a-'


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

"""
# @client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()
"""

@bot.command()
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await ctx.voice_client.disconnect()
    else:
        await ctx.content.send("The bot is not connected to a voice channel.")



async def action_to_voice_chat(message):
    if message.content == (ini_word + 'join voice chat'):
        await join(message)
    elif message.content == (ini_word + 'leave voice chat'):
        await leave(message)
