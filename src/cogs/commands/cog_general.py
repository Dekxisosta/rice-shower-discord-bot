from discord.ext import commands
from services.commands import general_service, help_service
from config.bot_defaults import DEFAULT_PREFIX
from datastore.static_data import config

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="greet", 
        description=config["general"]["commands"]["greet"]["desc"]
    )
    async def greet(self, ctx: commands.Context):
        await general_service.greet(
            ctx=ctx, 
            greetings=config["general"]["commands"]["greet"]["textlines"]
        )

    @commands.hybrid_command(
        name="help", 
        description=config["general"]["commands"]["help"]["desc"]
    )
    async def help(self, ctx: commands.Context):
        await help_service.help(
            ctx=ctx, 
            bot_prefix=DEFAULT_PREFIX, 
            config=config
        )

    @commands.hybrid_command(
        name="ping", 
        description=config["general"]["commands"]["ping"]["desc"]
    )
    async def ping(self, ctx: commands.Context):
        await general_service.ping(
            self.bot, 
            ctx=ctx, 
            format=config["general"]["commands"]["ping"]["format"]
        )

    @commands.hybrid_command(
        name="info", 
        description=config["general"]["commands"]["info"]["desc"]
    )
    async def info(self, ctx: commands.Context):
        await general_service.info(
            ctx=ctx, 
            info=config["general"]["commands"]["info"]["text"]
        )

    @commands.hybrid_command(name="quote", description=config["general"]["commands"]["quote"]["desc"])
    async def quote(self, ctx: commands.Context):
        await general_service.quote(
            ctx=ctx, 
            quotes=config["general"]["commands"]["quote"]["textlines"]
        )

    @commands.hybrid_command(name="umaline", description=config["general"]["commands"]["umaline"]["desc"])
    async def umaline(self, ctx: commands.Context):
        await general_service.umaline(
            ctx=ctx, 
            textlines=config["general"]["commands"]["umaline"]["textlines"]
        )

    @commands.hybrid_command(name="say", description=config["general"]["commands"]["say"]["desc"])
    async def say(self, ctx: commands.Context, *, msg: str):
        await general_service.say(ctx=ctx, msg=msg)

    @commands.hybrid_command(name="roll", description=config["general"]["commands"]["roll"]["desc"])
    async def roll(self, ctx: commands.Context):
        await general_service.roll(
            ctx=ctx, 
            format=config["general"]["commands"]["roll"]["format"]
        )

    @commands.hybrid_command(name="8ball", description=config["general"]["commands"]["8ball"]["desc"])
    async def eightBall(self, ctx: commands.Context, *, question: str):
        await general_service.eightBall(
            ctx=ctx, 
            question=question, 
            formatQuestion=config["general"]["commands"]["8ball"]["format-question"],
            formatResponse=config["general"]["commands"]["8ball"]["format-response"],
            responses=config["general"]["commands"]["8ball"]["textlines"]
        )

    @commands.hybrid_command(name="coinflip", description=config["general"]["commands"]["coinflip"]["desc"])
    async def coinflip(self, ctx: commands.Context):
        await general_service.coinflip(
            ctx=ctx, 
            format=config["general"]["commands"]["coinflip"]["format"]
        )

    @commands.hybrid_command(name="choose", description=config["general"]["commands"]["choose"]["desc"])
    async def choose(self, ctx: commands.Context, *, choices: str):
        await general_service.choose(
            ctx=ctx,
            input=choices,
            format=config["general"]["commands"]["choose"]["format"],
            fallback=config["general"]["commands"]["choose"]["fallback"],
            usage=config["general"]["commands"]["choose"]["usage"]
        )
    
async def setup(bot):
    await bot.add_cog(General(bot))