from discord.ext import commands
from services.commands import admin_only_service

class TopLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sync")
    @commands.has_permissions(administrator=True, manage_guild=True)
    @commands.guild_only()
    async def sync(self, ctx: commands.Context):
        await admin_only_service.sync(self.bot, ctx)

async def setup(bot):
    await bot.add_cog(TopLevel(bot))