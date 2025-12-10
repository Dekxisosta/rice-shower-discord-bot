import logging
import log.file_logger as file_logger
import utils.auto_loader as loader
from discord.ext import commands
from config.constants.defaults import DEFAULT_PREFIX, DEFAULT_TOKEN, DEFAULT_INTENTS
from config import directories as paths

logging.getLogger("discord").handlers = file_logger.setup_logger(logging.DEBUG).handlers

bot = commands.Bot(intents=DEFAULT_INTENTS, command_prefix=DEFAULT_PREFIX)

@bot.event
async def setup_hook():
    await loader.autoload_folder(bot, folder_path=paths.COMMANDS_FOLDER_PATH, package_prefix="cogs.commands")
    await loader.autoload_folder(bot, folder_path=paths.EVENTS_FOLDER_PATH, package_prefix="cogs.events")
    await bot.tree.sync()

if __name__ == "__main__":
    bot.run(
        DEFAULT_TOKEN,
        log_handler=None,  # keep None so discord.py uses our custom handlers
        log_level=logging.DEBUG
    )
