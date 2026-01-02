from discord import app_commands
from discord.ext import commands
from datastore.static_data import config

class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    automod = app_commands.Group(
        name="automod", 
        description= config["automod"]["desc"]
    )

async def setup(bot):
    await bot.add_cog(Automod(bot))