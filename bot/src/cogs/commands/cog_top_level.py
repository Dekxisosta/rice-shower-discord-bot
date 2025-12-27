from discord.ext import commands
from core.commands import top_level

class TopLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sync")
    @commands.is_owner()
    @commands.guild_only()
    async def sync(self, ctx: commands.Context):
        await top_level.sync(self.bot, ctx)

async def setup(bot):
    await bot.add_cog(TopLevel(bot))