import discord

roles = {
  '1️⃣': '１年生',
  '2️⃣': '2_year',
  '3️⃣': '3_year',
  '4️⃣': '4_year',
}

async def main(client, message):
  msg = await message.channel.send('リアクションを付けてください')
  for emoji in roles:
    await msg.add_reaction(emoji)

  def check(reaction, user):
    return user == message.author and str(reaction.emoji) in roles

  try:
    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
  except asyncio.TimeoutError:
    await message.channel.send('タイムアウトしました')
  else:
    role = discord.utils.get(message.guild.roles, name=roles[str(reaction.emoji)])
    await message.author.add_roles(role)
    await message.channel.send(f'{user.name}に{role.name}を付与しました')

if __name__ == '__main__':
  main()