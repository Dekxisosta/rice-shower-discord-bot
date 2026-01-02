from discord.abc import GuildChannel
from discord import Member
from typing import Iterable

class PermissionCtx():
    def __init__(
            self,
            bot: Member,
            caller: Member,
            bot_perms_required:Iterable[str], 
            caller_perms_required:Iterable[str],
            channel: GuildChannel | None = None,
            target: Member | None = None, 
            reason: str | None = None):
        
        self.channel = channel
        self.bot = bot
        self.caller = caller
        self.target = target
        self.reason = reason
        self.bot_perms_required = bot_perms_required
        self.caller_perms_required = caller_perms_required
        