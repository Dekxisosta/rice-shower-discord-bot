from discord.ext.commands import Context
from discord import Member
from typing import Iterable
from model import PermissionCtx

def convertCtxToPermCtx(
        ctx: Context,
        bot_perms_required: Iterable[str],
        caller_perms_required: Iterable[str],
        target: Member | None = None,
        reason: str | None = None) -> PermissionCtx:
    return PermissionCtx(
        channel=ctx.channel,
        bot=ctx.me,
        caller=ctx.author,
        bot_perms_required=bot_perms_required,
        caller_perms_required=caller_perms_required,
        target=target,
        reason=reason
    )