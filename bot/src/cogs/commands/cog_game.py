from discord import app_commands
from discord.ext import commands
from datastore.static_data import config

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    game = app_commands.Group(
        name="game", 
        description= config["game"]["desc"]
    )

async def setup(bot):
    await bot.add_cog(Game(bot))