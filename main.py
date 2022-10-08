import discord, asyncio
from datetime import datetime, timedelta
from discord.ext import commands
from discord import app_commands
import time
from time import sleep
import os
from dotenv import load_dotenv

#intents
intents = discord.Intents.default()
intents.message_content = True

#timer
def meetingtimer(number_of_seconds):
  if datetime.now()!=datetime.now() + timedelta(seconds=number_of_seconds):
    time.sleep(number_of_seconds)

#initialize client
load_dotenv()
TOKEN= os.getenv('DISCORD_TOKEN')
bot= commands.Bot(command_prefix= '!', intents= discord.Intents.default())

class Bot(commands.Bot):
  def __init__(self):
    intents= discord.Intents.all()
    intents.message_content= True
    super().__init__(command_prefix= "/", intents=intents)

  async def setup_hook(self):
   self.tree.copy_global_to(guild=discord.Object(id=1026654218104348682))
   await self.tree.sync()
   print("Slash commands have been synced!")

bot= Bot()

@bot.hybrid_command(name= 'setmeetingtime', description= 'Sets Meeting Time')
async def setmeetingtime(ctx:commands.Context, time_in_hours: float):
  await asyncio.sleep(time_in_hours*3600)
  await ctx.channel.send('Meeting has begun :wave:')


bot.run(TOKEN)