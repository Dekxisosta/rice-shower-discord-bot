from discord import app_commands
from discord.ext import commands
from datastore.static_data import config

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    utility = app_commands.Group(
        name="utility", 
        description= config["utility"]["desc"]
    )

async def setup(bot):
    await bot.add_cog(Utility(bot))