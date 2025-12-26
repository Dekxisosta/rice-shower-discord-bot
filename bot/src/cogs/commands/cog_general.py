from discord.ext import commands
from datastore.static_data import config
from core.commands import general

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_group(name=config["general"]["prefix"], invoke_without_command=True, with_app_command=True)
    async def prefix(self, ctx):
        await ctx.send(config["exception"]["invalid_command"])

    @prefix.command(name="greet", description=config["general"]["commands"]["greet"]["desc"])
    async def greet(self, ctx: commands.Context):
        await general.greet(ctx=ctx, greetings=config["general"]["commands"]["greet"]["textlines"])

    @prefix.command(name="help", description=config["general"]["commands"]["help"]["desc"])
    async def help(self, ctx: commands.Context):
        await general.help(ctx=ctx)

    @prefix.command(name="ping", description=config["general"]["commands"]["ping"]["desc"])
    async def ping(self, ctx: commands.Context):
        await general.ping(self.bot, ctx=ctx)

    @prefix.command(name="info", description=config["general"]["commands"]["info"]["desc"])
    async def info(self, ctx: commands.Context):
        await general.info(ctx=ctx, info=config["general"]["commands"]["info"]["text"])

    @prefix.command(name="quote", description=config["general"]["commands"]["quote"]["desc"])
    async def quote(self, ctx: commands.Context):
        await general.quote(ctx=ctx, quotes=config["general"]["commands"]["quote"]["textlines"])

    @prefix.command(name="say", description=config["general"]["commands"]["say"]["desc"])
    async def say(self, ctx: commands.Context, msg: str):
        await general.say(ctx=ctx, msg=msg)

async def setup(bot):
    await bot.add_cog(General(bot))