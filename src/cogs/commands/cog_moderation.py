from discord.ext import commands
from datastore.static_data import config
from services.commands import moderation_service
from utils.perms_tracker import check_eligibility_on_target
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_group(
        name=config["mod"]["prefix"],
        description=config["mod"]["desc"],
        invoke_without_command=True
    )
    async def moderation(self, ctx: commands.Context):
        await ctx.send("Available moderation commands:")

    @moderation.command(
        name="kick",
        description=config["mod"]["commands"]["kick"]["desc"]
    )
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        await moderation_service.kick(
            ctx=ctx,
            target=member,
            reason=reason,
            bot_perms_required=config["mod"]["commands"]["kick"]["bot-perms"],
            user_perms_required=config["mod"]["commands"]["kick"]["user-perms"]
        )



async def setup(bot):
    await bot.add_cog(Moderation(bot))