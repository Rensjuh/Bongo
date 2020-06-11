from discord.ext import commands

class TestCog:

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

    @commands.command()
    async def pick(self):
        self.counter += 1
        await self.bot.say('Bongo is nu %d geaaid!' % self.counter)


def setup(bot):
    bot.add_cog(TestCog(bot))