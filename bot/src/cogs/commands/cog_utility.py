from discord import app_commands
from discord.ext import commands
from resources.descriptions.utility_command_desc import DESC

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    utility = app_commands.Group(
        name="utility", 
        description= DESC["main"]
    )

async def setup(bot):
    await bot.add_cog(Utility(bot))