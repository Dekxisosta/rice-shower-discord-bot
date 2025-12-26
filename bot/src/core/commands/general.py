from discord.ext import commands
from assets.embeds.help import help_group as help_embed

# Greet Command : Randomly picks a greeting line
async def greet(ctx: commands.Context, greetings: list[str]):
    import random
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(random.choice(greetings))
    else:
        await ctx.send(random.choice(greetings))
        
# Help Command : Shows a list of available commands
async def help(ctx: commands.Context, bot_prefix: str, group_prefix: str, commands: dict):
    embeds, files = help_embed.create(bot_prefix = bot_prefix, group_prefix=group_prefix, commands=commands)
        
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
async def info(ctx:commands.Context, info: str):
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(info, ephemeral = True)
    else:
        await ctx.send(info)

# Quote Command : Randomly says whatever quote that is unique to Rice Shower's traits
async def quote(ctx:commands.Context, quotes: list[str]):
    import random
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(random.choice(quotes), ephemeral = True)
    else:
        await ctx.send(random.choice(quotes))

# Say Command : Says the message the user wants Rice Shower to say
async def say(ctx:commands.Context, msg: str):
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg, ephemeral = True)
    else:
        await ctx.send(msg)