from discord import app_commands
from discord.ext import commands
from datastore.static_data import config

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    management = app_commands.Group(
        name="management", 
        description= config["manage"]["desc"]
    )

async def setup(bot):
    await bot.add_cog(Management(bot))