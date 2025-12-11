from discord import app_commands
from discord.ext import commands
from resources.descriptions.mod_command_desc import DESC

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    moderation = app_commands.Group(
        name="moderation", 
        description= DESC["main"]
    )

async def setup(bot):
    await bot.add_cog(Moderation(bot))