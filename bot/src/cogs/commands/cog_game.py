from discord import app_commands
from discord.ext import commands
from bot.src.resources.descriptions.game_desc import DESC

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    game = app_commands.Group(
        name="game", 
        description= DESC["main"]
    )

async def setup(bot):
    await bot.add_cog(Game(bot))