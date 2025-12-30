from discord.ext import commands
from factories.help_group_factory import create_group as create_help_group
from ui.page_view import PageView
from discord.ext import commands

# Greet Command : Randomly picks a greeting line
async def greet(ctx: commands.Context, greetings: list[str]):
    import random
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(random.choice(greetings))
    else:
        await ctx.send(random.choice(greetings))

# Ping Command : Shows Rice Shower's response time
async def ping(bot, ctx: commands.Context, format: str):
    msg = format.format(round(bot.latency*1000))
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg)
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
        await ctx.interaction.response.send_message(random.choice(quotes))
    else:
        await ctx.send(random.choice(quotes))

# Umaline Command : Randomly says an in-game Rice Shower voiceline as text
async def umaline(ctx:commands.Context, textlines: list[str]):
    import random
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(random.choice(textlines))
    else:
        await ctx.send(random.choice(textlines))

# Say Command : Says the message the user wants Rice Shower to say
async def say(ctx:commands.Context, msg: str):
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg)
    else:
        await ctx.send(msg)

# Coinflip Command : Chooses a number at random 1-2
async def coinflip(ctx:commands.Context, format: str):
    import random
    msg = format.format(outcome = random.choice(["heads", "tails"]))
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg)
    else:
        await ctx.send(msg)
        
# Roll Command : Chooses a number at random 1-6
async def roll(ctx:commands.Context, format: str):
    import random
    msg = format.format(outcome = random.randint(1,6))
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg)
    else:
        await ctx.send(msg)

# 8ball Command : Determine fortune
async def eightBall(ctx:commands.Context, question: str, formatQuestion: str, formatResponse: str, responses: list):
    import random
    msg = formatResponse.format(random.choice(responses))
    if ctx.interaction is not None:
        msg = formatQuestion.format(question=question) + "\n" + msg
        await ctx.interaction.response.send_message(msg)
    else:
        await ctx.send(msg)

# Choose Command : Choose from a list of options
async def choose(ctx:commands.Context, input: str, format: str, fallback: str, usage: str):
    sep = "|" if "|" in input else ","
    choices = [opt.strip() for opt in input.split(sep) if opt.strip()]

    msg = ""
    if len(choices) < 2:
        msg = f"{fallback}\nExample: {usage}"
    else:
        import random
        msg = format.format(random.choice(choices))

    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg)
    else:
        await ctx.send(msg)

# Help Command : Shows a list of available commands
async def help(ctx: commands.Context, bot_prefix: str, config: dict):
    groups = [
        create_help_group(
            desc=config["general"]["desc"],
            commands=config["general"]["commands"],
        ),
        create_help_group(
            desc=config["mod"]["desc"],
            commands=config["mod"]["commands"],
            group_prefix=config["mod"]["prefix"]
        ),
        create_help_group(
            desc=config["automod"]["desc"],
            commands=config["automod"]["commands"],
            group_prefix=config["automod"]["prefix"]
        )
    ]
    
    view = PageView(groups)

    if ctx.interaction is not None:
        await ctx.interaction.response.defer()
        await ctx.interaction.followup.send(embed=groups[0].embed, view=view, ephemeral=True)
    else:
        await ctx.send(embed=groups[0].embed, view=view)



    
