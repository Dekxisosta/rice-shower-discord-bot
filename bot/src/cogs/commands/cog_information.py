from discord import app_commands
from discord.ext import commands
from datastore.static_data import config

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    information = app_commands.Group(
        name="information", 
        description= config["info"]["desc"]
    )

async def setup(bot):
    await bot.add_cog(Information(bot))