import logging
import log.file_logger as file_logger
import utils.auto_loader as loader
from discord.ext import commands
from config.constants.defaults import DEFAULT_PREFIX, DEFAULT_TOKEN, DEFAULT_INTENTS
from config.paths import folder_paths
import discord

logging.getLogger("discord").handlers = file_logger.setup_logger(logging.DEBUG).handlers

bot = commands.Bot(
    intents=DEFAULT_INTENTS, 
    command_prefix=DEFAULT_PREFIX,
    help_command=None
)

@bot.event
async def setup_hook():
    await loader.autoload_folder(bot, folder_path=folder_paths.COMMANDS_FOLDER_PATH, package_prefix="cogs.commands")
    await loader.autoload_folder(bot, folder_path=folder_paths.EVENTS_FOLDER_PATH, package_prefix="cogs.events")
    await bot.tree.sync()
    for cmd in bot.tree.get_commands():
        print(cmd.name)
        if hasattr(cmd, "commands"):
            for sub in cmd.commands:
                print("  └─", sub.name)

@bot.command(name="Sync", description="Sync slash commands")
@commands.is_owner()
@commands.guild_only()
async def sync(ctx: commands.Context):
    ctx.bot.tree.clear_commands(guild=ctx.guild)
    ctx.bot.tree.copy_global_to(guild=ctx.guild)
    synced = await ctx.bot.tree.sync(guild=ctx.guild)
    print(synced)
    await ctx.reply(f"Synced {len(synced)} commands", mention_author=False)

if __name__ == "__main__":
    bot.run(
        DEFAULT_TOKEN,
        log_handler=None,
        log_level=logging.DEBUG,
    )
