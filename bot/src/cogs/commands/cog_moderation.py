from discord import app_commands
from discord.ext import commands
from bot.src.resources.descriptions.mod_desc import DESC

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    moderation = app_commands.Group(
        name="moderation", 
        description= DESC["main"]
    )

async def setup(bot):
    await bot.add_cog(Moderation(bot))