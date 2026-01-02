from typing import Iterable, Callable, Awaitable
from model import PermissionCtx
from discord.abc import GuildChannel
from discord import Member, NotFound, Object, Guild

# ==================================
# PUBLIC API
# ==================================

# Checks eligibility of the given command context
async def check_eligibility_on_target(
        permctx: PermissionCtx,
        send: Callable[[str], Awaitable[None]]) -> bool:
    if not await _check_if_guild(send=send):
        return False
    
    if permctx.target == permctx.channel.guild.owner:
        await send("Cannot perform command, intended target is the guild owner")
        return False
    
    if permctx.target.top_role >= permctx.caller.top_role:
        await send("Cannot perform command, intended target is of greater or equal role hierarchy than you")
        return False

    if permctx.target.top_role >= permctx.bot.author.top_role:
        await send("Cannot perform command, intended target is of greater or equal role hierarchy than bot")
        return False

    if not await check_perms(
        permctx=permctx,
        send=send
        ):
        return False
    
    return True

# Checks permissions of the given command context
async def check_perms(
        permctx: PermissionCtx,
        send: Callable[[str], Awaitable[None]]) -> bool:
    missing_user = _validate_perms(channel=permctx.channel, member=permctx.caller, required=permctx.caller_perms_required)
    if missing_user:
        await send("Cannot perform command, user permissions do not suffice in this context")
        return False
    
    missing_bot = _validate_perms(channel=permctx.channel, member=permctx.bot, required=permctx.bot_perms_required)
    if missing_bot:
        await send("Cannot perform command, bot permissions do not suffice in this context")
        return False
    
    return True

# Checks if a user is banned in a guild
async def is_user_banned(
        guild: Guild, 
        user_id: int) -> bool:
    try:
        await guild.fetch_ban(Object(id=user_id))
        return True
    except NotFound:
        return False

# ==================================
# INTERNAL HELPERS
# ==================================

# Checks if the command context is used in a channel's guild
async def _check_if_guild(
        permctx: PermissionCtx, 
        send: Callable[[str], Awaitable[None]]) -> bool:
    if permctx.channel.guild is None:
        await send("Cannot perform command, only effective in discord servers")
        return False
    return True

# Checks validity of perms by comparing existing channel perms to required perms
def _validate_perms(
    channel: GuildChannel,
    member: Member,
    required: Iterable[str]) -> list[str]:
    perms = channel.permissions_for(member)
    return [p for p in required if not getattr(perms, p, False)]