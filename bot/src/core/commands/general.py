from discord.ext import commands
from config import commands as configs

import yaml
with open ("config/commands/configs")

from resources.embeds.help_menu import get_embed
from resources.textlines.greetings import LINES as greetings
from resources.textlines.quotes import LINES as quotes

# Greet Command : Randomly picks a greeting line
async def greet(ctx: commands.Context):
    import random
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(random.choice(greetings))
    else:
        await ctx.send(random.choice(greetings))
        
# Help Command : Shows a list of available commands
async def help(ctx: commands.Context):
    embeds, files = get_embed()
        
    if ctx.interaction is not None:
        await ctx.interaction.response.defer()
        await ctx.interaction.followup.send(embeds=embeds, files=files, ephemeral=True)
    else:
        await ctx.send(embeds=embeds, files=files)

# Ping Command : Shows Rice Shower's response time
async def ping(bot, ctx: commands.Context):
    msg = f"P-pong! 🏓 Latency is {round(bot.latency * 1000)}ms."
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg, ephemeral = True)
    else:
        await ctx.send(msg)

# Info Command : Tells information about the bot
async def info(ctx:commands.Context):
    msg = "Rice Shower is a friendly server bot that only supports general commands for now"
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg, ephemeral = True)
    else:
        await ctx.send(msg)

# Quote Command : Randomly says whatever quote that is unique to Rice Shower's traits
async def quote(ctx:commands.Context):
    import random
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(random.choice(quotes), ephemeral = True)
    else:
        await ctx.send(random.choice(quotes))

# Say Command : Says the message the user wants Rice Shower to say
async def say(msg: str, ctx:commands.Context):
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg, ephemeral = True)
    else:
        await ctx.send(msg)