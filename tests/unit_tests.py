import pytest
import asyncio

from src.model import PermissionCtx
from src.utils import check_eligibility_on_target, check_perms
from tests.fakes import FakeMember, FakeChannel, FakeGuild, FakePermissions, SendRecorder

# --------------------------
# Test helpers
# --------------------------
def make_ctx(
    me_role=10, caller_role=5, target_role=6,
    bot_perms=None, caller_perms=None
):
    owner = FakeMember(99)
    guild = FakeGuild(owner=owner)

    me = FakeMember(me_role, name="me")
    caller = FakeMember(caller_role, name="caller")
    target = FakeMember(target_role, name="target")

    perms_dict = {
        me: FakePermissions(**(bot_perms or {})),
        caller: FakePermissions(**(caller_perms or {}))
    }

    channel = FakeChannel(guild, perms_dict)

    return PermissionCtx(
        me=me,
        caller=caller,
        target=target,
        channel=channel,
        bot_perms_required=list(bot_perms or []),
        caller_perms_required=list(caller_perms or []),
        reason=None
    )

# --------------------------
# Tests
# --------------------------
@pytest.mark.asyncio
async def test_target_higher_than_caller():
    ctx = make_ctx(caller_role=5, target_role=6)
    send = SendRecorder()

    result = await check_eligibility_on_target(ctx, send)
    assert result is False
    assert any("greater or equal role hierarchy" in msg for msg in send.messages)

@pytest.mark.asyncio
async def test_target_higher_than_me():
    ctx = make_ctx(me_role=5, target_role=6)
    send = SendRecorder()

    result = await check_eligibility_on_target(ctx, send)
    assert result is False
    assert any("greater or equal role hierarchy than bot" in msg for msg in send.messages)

@pytest.mark.asyncio
async def test_pass_all_checks():
    ctx = make_ctx(me_role=10, caller_role=5, target_role=4, bot_perms={"manage_messages": True}, caller_perms={"send_messages": True})
    send = SendRecorder()

    result = await check_eligibility_on_target(ctx, send)
    assert result is True
    assert send.messages == []

@pytest.mark.asyncio
async def test_check_perms_missing_caller():
    ctx = make_ctx(bot_perms={"manage_messages": True}, caller_perms={})
    send = SendRecorder()

    # Require caller to have send_messages which they don't
    ctx.caller_perms_required = ["send_messages"]

    result = await check_perms(ctx, send)
    assert result is False
    assert any("user permissions do not suffice" in msg for msg in send.messages)

@pytest.mark.asyncio
async def test_check_perms_missing_bot():
    ctx = make_ctx(bot_perms={"manage_messages": False}, caller_perms={"send_messages": True})
    send = SendRecorder()

    # Require bot to have manage_messages which it doesn't
    ctx.bot_perms_required = ["manage_messages"]

    result = await check_perms(ctx, send)
    assert result is False
    assert any("bot permissions do not suffice" in msg for msg in send.messages)
    