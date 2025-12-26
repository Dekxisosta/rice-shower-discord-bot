import logging
import log.file_logger as file_logger
import utils.auto_loader as loader
from discord.ext import commands
from bot.src.config.bot_defaults import DEFAULT_PREFIX, DEFAULT_TOKEN, DEFAULT_INTENTS
from config.paths import folder_paths

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

if __name__ == "__main__":
    bot.run(
        DEFAULT_TOKEN,
        log_handler=None,
        log_level=logging.DEBUG,
    )
