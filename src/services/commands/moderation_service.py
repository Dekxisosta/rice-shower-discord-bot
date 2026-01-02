from utils.perms_tracker import check_eligibility_on_target, check_perms, is_user_banned
from utils.message_sender import send_ephemeral
from discord.ext.commands import Context
from typing import Iterable, Callable, Awaitable
from discord import Member, User
    
# Kicks a member based on filters from passed lists of required discord perms
async def kick(
        target:Member, reason:str, 
        send: Callable[[str], Awaitable[None]],
        bot_perms_required:Iterable[str],
        user_perms_required:Iterable[str]):
    if await check_eligibility_on_target(ctx=ctx, target=target, bot_perms_required=bot_perms_required, user_perms_required=user_perms_required):
        await target.kick(reason=reason)
        await send(msg=f"Successfully kicked {target.mention}")


# Bans a member based on filters from passed lists of required discord perms
async def ban(ctx:Context, target:User, reason:str, bot_perms_required:Iterable[str], user_perms_required:Iterable[str]):
    if not await check_eligibility_on_target(ctx=ctx, target=target, bot_perms_required=bot_perms_required, user_perms_required=user_perms_required):
        return
    if await is_user_banned(guild=ctx.guild, user_id=target.id):
        await send_ephemeral(ctx=ctx, msg=f"{target.name} is already banned")
        return
    
    await target.ban(reason=reason)
    await send_ephemeral(ctx=ctx, msg=f"Successfully banned {target.mention}")

# Unbans a member based on filters from passed lists of required discord perms
async def unban(ctx:Context, target:User, reason:str, bot_perms_required:Iterable[str], user_perms_required:Iterable[str]):
    if not await check_eligibility_on_target(ctx=ctx, target=target, bot_perms_required=bot_perms_required, user_perms_required=user_perms_required):
        return
    if not await is_user_banned(guild=ctx.guild, user_id=target.id):
        await send_ephemeral(ctx=ctx, msg=f"{target.name} is not banned")
        return
    
    await target.unban(reason=reason)
    await send_ephemeral(ctx=ctx, msg=f"Successfully unbanned {target.mention}")

# Purges messages in a channel
async def purge(ctx: Context,amount:int, bot_perms_required: Iterable[str], user_perms_required:Iterable[str]):
    if not await check_perms(ctx=ctx,  bot_perms_required=bot_perms_required, user_perms_required=user_perms_required):
        return 
    if amount<=0:
        await send_ephemeral(ctx=ctx, msg="Amount must be greater than 0")
        return
    deleted = await ctx.channel.purge(limit=amount+1)
    await send_ephemeral(ctx=ctx, msg=f"Deleted {deleted} messages in {ctx.channel.name}")


    
    
    