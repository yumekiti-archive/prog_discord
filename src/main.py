import discord
from discord.ext import commands
import role

import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')

@bot.command()
async def join(ctx):
  await role.join(ctx)

bot.run(os.getenv('TOKEN'))