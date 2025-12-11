from discord import app_commands
from discord.ext import commands
from resources.descriptions.automod_command_desc import DESC

class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    automod = app_commands.Group(
        name="automod", 
        description= DESC["main"]
    )

async def setup(bot):
    await bot.add_cog(Automod(bot))