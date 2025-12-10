import discord
from discord import app_commands
from discord.ext import commands
from resources import responses

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="greet", description="Rice Shower greets you!")
    async def greet(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "H-hi! Rice Shower is here! 💐"
        )

    @app_commands.command(name="help", description="U-Um… I gathered all my commands here… I hope they're useful to you…")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            embed=responses.RICE_MENU_EMBED,
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(General(bot))