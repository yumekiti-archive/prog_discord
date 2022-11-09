from datetime import datetime, time

from discord.ext import commands, tasks

import main
import write
import os

prog_channel_id = 1026376855969865840
attend_time = time(hour=17)
recode_time = time(hour=20)
report_day = '01'
attendance_enojis = ['👍', '👎']


class Task(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  def cog_unload(self):
    self.attend.cancel()
    self.record.cancel()

  async def cog_load(self):
    self.prog_channel = self.bot.get_channel(prog_channel_id)
    if self.prog_channel is None:
      self.prog_channel = await self.bot.fetch_channel(prog_channel_id)
    self.record.start()
    self.attend.start()

  @tasks.loop(minutes=1)
  async def attend(self):
    if f'{datetime.now():%H%M}' != f'{attend_time:%H%M}':
      return
    message = await self.prog_channel.send(f'{datetime.now().strftime("%Y/%m/%d")}です、出席しますか？')

    for emoji in attendance_enojis:
      await message.add_reaction(emoji)

    today = datetime.now().strftime("%Y/%m/%d")
    while today == datetime.now().strftime("%Y/%m/%d"):
      reaction, user = await self.bot.wait_for('reaction_add')
      if reaction.emoji == '👍' and not user.bot:
        roles = [role.name for role in user.roles]
        await write.main(self.prog_channel, [], {'name': user.name, 'roles': roles})

  @tasks.loop(minutes=1)
  async def record(self):
    if f'{datetime.now():%H%M}' != f'{recode_time:%H%M}':
      return
    await write.record()
    await self.prog_channel.send("本日の活動内容を記録しました。")

  @tasks.loop(hours=24)
  async def record(self):
    if f'{datetime.now():%d}' != f'{report_day}':
      return
    os.system(f'/usr/bin/python3 ./src/report.py {datetime.now():%Y-%m}')

async def setup(bot: commands.Bot):
  await bot.add_cog(Task(bot))
