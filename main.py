import discord
import role

import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/join'):
    await role.join(client, message)

@client.event
async def on_member_join(member):
  await role.join(client, member)

client.run(os.getenv('TOKEN'))