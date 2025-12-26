from discord import app_commands
from discord.ext import commands
from datastore.static_data import config

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    moderation = app_commands.Group(
        name="moderation", 
        description= config["mod"]["desc"]
    )

async def setup(bot):
    await bot.add_cog(Moderation(bot))