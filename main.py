import discord
from discord import commands
from discord import guilds
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

import os
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN= os.getenv('DISCORD_TOKEN')
client= commands.Bot(c_l= '/')

@client.comman

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #to prevent bot from replying to itself
  if message.author== client.user:
    return

    
  elif message.content== '$hello':
    await message.channel.send('bruh')


client.run(TOKEN)