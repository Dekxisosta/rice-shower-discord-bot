from discord import app_commands
from discord.ext import commands
from bot.src.resources.descriptions.manage_desc import DESC

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    management = app_commands.Group(
        name="management", 
        description= DESC["main"]
    )

async def setup(bot):
    await bot.add_cog(Management(bot))