import discord

roles = {
  '1️⃣': '1_year',
  '2️⃣': '2_year',
  '3️⃣': '3_year',
  '4️⃣': '4_year',
}

async def main(ctx):
  for emoji in roles.keys():
    await ctx.message.add_reaction(emoji)

  def check(reaction, user):
    return user == ctx.author and str(reaction.emoji) in roles.keys()

  try:
    reaction, user = await ctx.bot.wait_for('reaction_add', timeout=60.0, check=check)
  except asyncio.TimeoutError:
    await ctx.send('タイムアウトしました。')
  else:
    role = discord.utils.get(ctx.guild.roles, name=roles[str(reaction.emoji)])
    await ctx.author.add_roles(role)

    await ctx.send(f'{ctx.author.name}さんの学年を{role.name}に設定しました。')

    for role in ctx.author.roles:
      if role.name in roles.values() and role.name != roles[str(reaction.emoji)]:
        await ctx.author.remove_roles(role)

    await ctx.message.clear_reactions()
