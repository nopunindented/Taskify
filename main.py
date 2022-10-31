import discord, asyncio
from datetime import datetime, timedelta
from webserver import keep_alive
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

#intents
intents = discord.Intents.default()
intents.message_content = True

""""
def meetingtimer(number_of_seconds):
  if datetime.now()!=datetime.now() + timedelta(seconds=number_of_seconds):
    time.sleep(number_of_seconds)
    """

#initialize client
load_dotenv()
TOKEN= os.getenv('DISCORD_TOKEN')
bot= commands.Bot(command_prefix= '/', intents= discord.Intents.default())

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


@bot.hybrid_group(name= 'meetingtimescommands', fallback="get")
async def meetings(ctx:commands.Context):
  await ctx.send("Setting Meeting Time")

@meetings.command()
async def setmeetingtime1role(ctx:commands.Context, time_in_hours: float, role: discord.Role):
  await asyncio.sleep(time_in_hours*3600)
  await ctx.channel.send(f"{role.mention} the meeting has begun! :wave:")

@meetings.command()
async def setmeetingtime2roles(ctx:commands.Context, time_in_hours: float, role: discord.Role,role2: discord.Role):
  await asyncio.sleep(time_in_hours*3600)
  await ctx.channel.send(f"{role.mention} {role2.mention} the meeting has begun! :wave:")

@meetings.command()
async def setmeetingtime3roles(ctx:commands.Context, time_in_hours: float, role: discord.Role,role2: discord.Role,role3: discord.Role):
  await asyncio.sleep(time_in_hours*3600)
  await ctx.channel.send(f"{role.mention} {role2.mention} {role3.mention} the meeting has begun! :wave:")

@meetings.command()
async def setmeetingtime4roles(ctx:commands.Context, time_in_hours: float, role: discord.Role,role2: discord.Role,role3: discord.Role, role4: discord.Role):
  await asyncio.sleep(time_in_hours*3600)
  await ctx.channel.send(f"{role.mention} {role2.mention} {role3.mention} {role4.mention} the meeting has begun! :wave:")

@meetings.command()
async def setmeetingtime5roles(ctx:commands.Context, time_in_hours: float, role: discord.Role,role2: discord.Role,role3: discord.Role,role4: discord.Role,role5: discord.Role):
  await asyncio.sleep(time_in_hours*3600)
  await ctx.channel.send(f"{role.mention} {role2.mention} {role3.mention} {role4.mention} {role5.mention} the meeting has begun! :wave:")

@bot.hybrid_group(name= 'eventtime', fallback="get")
async def eventss(ctx:commands.Context):
  await ctx.send("Set Event Time")

@eventss.command()
async def seteventandtime(ctx:commands.Context, event_name: str,event_time_in_hours: int):
  global event_is
  event_is= event_name
  global time_remaining
  time_remaining= event_time_in_hours
  for i in range(0, event_time_in_hours*3600):
    time_remaining= event_time_in_hours-(1/3600)
    round(time_remaining, 4)
    await asyncio.sleep(1)

@eventss.command()
async def checkremainingtimeinevent(ctx:commands.Context):
  await ctx.channel.send(f"The time remaining for the {event_is} event is {time_remaining}!")
  
"""datetimetinkering

  now= datetime.now()
  hourized=now.strftime("%H:%M:%S")
  newtime= now + timedelta(time_in_hours*3600)
  newtimed= newtime.strftime("%H:%M:%S")
"""
keep_alive()
bot.run(TOKEN)