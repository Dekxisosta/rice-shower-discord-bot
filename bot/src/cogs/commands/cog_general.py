from discord.ext import commands
from resources.descriptions.general_command_desc import DESC
from core.commands import general

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_group(name="rs", invoke_without_command=True, with_app_command=True)
    async def rs(self, ctx):
        await ctx.send("Use `rs greet`")

    # ===============---------
    # Greet
    # ===============---------
    @rs.command(name="greet", description=DESC["greet"])
    async def greet(self, ctx: commands.Context):
        await general.greet(ctx=ctx)

    # ===============---------
    # Help
    # ===============---------
    @rs.command(name="help", description=DESC["help"])
    async def help(self, ctx: commands.Context):
        await general.help(ctx=ctx)

    # ===============---------
    # Ping
    # ===============---------
    @rs.command(name="ping", description=DESC["ping"])
    async def ping(self, ctx: commands.Context):
        await general.ping(self.bot, ctx=ctx)

    # ===============---------
    # Info
    # ===============---------
    @rs.command(name="info", description=DESC["info"])
    async def info(self, ctx: commands.Context):
        await general.info(ctx=ctx)

    # ===============---------
    # Quote
    # ===============---------
    @rs.command(name="quote", description=DESC["quote"])
    async def quote(self, ctx: commands.Context):
        await general.quote(ctx=ctx)

    # ===============---------
    # Say
    # ===============---------
    @rs.command(name="say", description=DESC["say"])
    async def say(self, ctx: commands.Context, msg: str):
        await general.say(msg, ctx=ctx)

async def setup(bot):
    await bot.add_cog(General(bot))