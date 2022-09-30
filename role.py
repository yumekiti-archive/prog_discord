import discord

roles = {
  '1️⃣': '１年生',
  '2️⃣': '2_year',
  '3️⃣': '3_year',
  '4️⃣': '4_year',
}

async def on_member_join(client, message):
  for emoji in roles.keys():
    await message.add_reaction(emoji)

  def check(reaction, user):
    return user == message.author and str(reaction.emoji) in roles.keys()

  try:
    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
  except asyncio.TimeoutError:
    await message.channel.send('タイムアウトしました')
  else:
    role = discord.utils.get(message.guild.roles, name=roles[str(reaction.emoji)])
    await message.author.add_roles(role)

    for r in message.author.roles:
      if r.name in roles.values() and r.name != roles[str(reaction.emoji)]:
        await message.author.remove_roles(r)

    await message.channel.send(f'{message.author.mention} に {role.name} を付与しました')
    await message.clear_reactions()

if __name__ == '__main__':
  main()