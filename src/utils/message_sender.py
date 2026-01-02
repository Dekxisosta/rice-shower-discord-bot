from discord.ext.commands import Context

# Sends a publicized message
async def send_message(ctx: Context, msg: str, delete_invoke: bool = False) -> None:
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg)
    else:
        if delete_invoke:
            await ctx.message.delete()
        await ctx.send(msg)

# Sends a disappearing/ephemeral message
async def send_ephemeral(ctx: Context, msg: str, delete_invoke: bool = True, delete_after: float = 5) -> None:
    if ctx.interaction is not None:
        await ctx.interaction.response.send_message(msg, ephemeral=True)
    else:
        if delete_invoke:
            await ctx.message.delete()
        await ctx.send(msg, delete_after=delete_after)