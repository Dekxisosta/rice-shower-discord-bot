"""
Fakes for testing permission/service logic
without needing a live Discord bot.
"""

# --------------------------
# Roles / Members
# --------------------------
class FakeRole:
    """Minimal stand-in for discord.Role"""
    def __init__(self, position: int):
        self.position = position

    def __ge__(self, other: "FakeRole"):
        return self.position >= other.position


class FakeMember:
    """Minimal stand-in for discord.Member"""
    def __init__(self, top_role_position: int, *, name: str = "", is_owner: bool = False):
        self.top_role = FakeRole(top_role_position)
        self.name = name
        self._is_owner = is_owner

    def __eq__(self, other):
        return self is other

# --------------------------
# Permissions
# --------------------------
class FakePermissions:
    """Fake permissions object for channel.permissions_for"""
    def __init__(self, **perms):
        for k, v in perms.items():
            setattr(self, k, v)

# --------------------------
# Channel / Guild
# --------------------------
class FakeGuild:
    """Minimal stand-in for discord.Guild"""
    def __init__(self, owner: FakeMember):
        self.owner = owner

class FakeChannel:
    """Minimal stand-in for discord.abc.GuildChannel"""
    def __init__(self, guild: FakeGuild, perms: dict[FakeMember, FakePermissions] | None = None):
        self.guild = guild
        self._perms = perms or {}

    def permissions_for(self, member: FakeMember):
        return self._perms.get(member, FakePermissions())

# --------------------------
# Send recorder
# --------------------------
class SendRecorder:
    """Async callable to capture send() messages"""
    def __init__(self):
        self.messages: list[str] = []

    async def __call__(self, message: str):
        self.messages.append(message)