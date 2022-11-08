from datetime import datetime, time

from discord.ext import commands, tasks

import main
import write

prog_channel_id = 1026376855969865840
attend_time = time(hour=17)
recode_time = time(hour=20)


class Task(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.attend.start()
        self.record.start()

    async def cog_load(self):
        self.prog_channel = self.bot.get_channel(prog_channel_id)
        if self.prog_channel is None:
            self.prog_channel = await self.bot.fetch_channel(prog_channel_id)

    @tasks.loop(time=attend_time)
    async def attend(self):
        main.attend(self.prog_channel)

    @tasks.loop(time=recode_time)
    async def record(self):
        await self.prog_channel.send("本日の活動内容を記録しました。")


async def setup(bot: commands.Bot):
    bot.add_cog(Task(bot))
