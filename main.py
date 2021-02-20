# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import discord
from discord.ext import commands
import nest_asyncio
nest_asyncio.apply()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('--bawa'):
        await message.channel.send('Betee... Betee... Oo bete mauj kardi.. Are tum to bade hevy driver ho')

    elif message.content.startswith('--pawri'):
        await message.channel.send('Ye humari pawri ho rahi hai.. 🎉')
    
    elif message.content.startswith('--meme'):  
        await message.channel.send(file=discord.File('meme.jpg'))

client.run(TOKEN)
        