import discord
from discord.ext import commands
from datetime import datetime

import role_add
import attendance

import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')

@bot.command()
async def role(ctx):
  await role_add.main(ctx)

@bot.command()
async def attend(ctx):
  role_names = [role.name for role in ctx.author.roles]
  name = ctx.author.name
  if len(ctx.message.content.split()) > 1:
    body = { "name": name, "content": ctx.message.content.split()[1] }
  else: body = []
  await attendance.main(
    ctx,
    datetime.now(),
    body,
    "2302",
    { 'name': name, 'roles': role_names }
  )

bot.run(os.getenv('TOKEN'))
