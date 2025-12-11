from discord import app_commands
from discord.ext import commands
from resources.descriptions.info_command_desc import DESC

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    information = app_commands.Group(
        name="information", 
        description= DESC["main"]
    )

async def setup(bot):
    await bot.add_cog(Information(bot))