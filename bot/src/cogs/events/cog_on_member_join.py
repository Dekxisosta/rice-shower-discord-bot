from discord.ext import commands
# from data import session_data as db

class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(OnMemberJoin(bot))