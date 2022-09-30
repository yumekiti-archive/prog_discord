# This example requires the 'message_content' intent.

import discord
import role

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

  if message.content.startswith('/role'):
    await role.main(client, message)

client.run('MTAyNTIwNTk1MDE0OTMwMDIzNA.GJDt5G.PwoPboXiOlFe6ayLS_ik1o2PT6ZgykN81gEBsQ')