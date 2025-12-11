import discord
from discord import app_commands
from discord.ext import commands
from resources.descriptions.general_command_desc import DESC

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    general = app_commands.Group(
        name="general",
        description=DESC["main"]
    )

    # Greet command
    @general.command(name="greet", description=DESC["greet"])
    async def greet(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "H-hi! Rice Shower is here! 💐"
        )

    # Help command
    @general.command(name="help", description=DESC["help"])
    async def help(self, interaction: discord.Interaction):
        help_text = (
            "**Rice Commands:**\n"
            "/main - Introduction to Rice\n"
            "/greet - Rice says hello\n"
            "/ping - Check latency\n"
            "/info - Info about Rice Shower\n"
            "/quote - Get a random quote\n"
            "/say - Make Rice say something\n"
        )
        await interaction.response.send_message(help_text)

    # Ping command
    @general.command(name="ping", description=DESC["ping"])
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"P-pong! 🏓 Latency is {latency}ms.")

    # Info command
    @general.command(name="info", description=DESC["info"])
    async def info(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Rice Shower is a friendly server bot that helps with commands, mini-games, and general fun! 🎀"
        )

    # Quote command
    @general.command(name="quote", description=DESC["quote"])
    async def quote(self, interaction: discord.Interaction):
        import random
        quotes = [
            "Keep going, you're doing great! 🌟",
            "A smile a day keeps the gloom away! 😊",
            "Believe in yourself, always! 💖",
        ]
        await interaction.response.send_message(random.choice(quotes))

    # Say command
    @general.command(name="say", description=DESC["say"])
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(f"{message}")
    


async def setup(bot):
    await bot.add_cog(General(bot))