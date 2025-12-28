from discord.ext import commands


async def clear_commands(bot, ctx: commands.Context):
    ctx.bot.tree.clear_commands(guild=ctx.guild)
    await ctx.bot.tree.sync(guild=ctx.guild)

async def sync(bot, ctx: commands.Context):
    bot.tree.clear_commands(guild=ctx.guild)
    bot.tree.copy_global_to(guild=ctx.guild)
    synced = await bot.tree.sync(guild=ctx.guild)
    await ctx.send(f"✅ Synced {len(synced)} commands to **{ctx.guild.name}**")