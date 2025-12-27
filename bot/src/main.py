import logging
import log.file_logger as file_logger
import utils.auto_loader as loader
from discord.ext import commands
from config.bot_defaults import DEFAULT_PREFIX, DEFAULT_TOKEN, DEFAULT_INTENTS
from config.directories import COMMANDS_FOLDER_PATH, EVENTS_FOLDER_PATH
from bootstrapper import config_loader

logging.getLogger("discord").handlers = file_logger.setup_logger(logging.DEBUG).handlers
config_loader.load()

bot = commands.Bot(
    intents=DEFAULT_INTENTS, 
    command_prefix=DEFAULT_PREFIX,
    help_command=None
)

@bot.event
async def setup_hook():
    await loader.autoload_folder(bot, folder_path=COMMANDS_FOLDER_PATH, package_prefix="cogs.commands")
    await loader.autoload_folder(bot, folder_path=EVENTS_FOLDER_PATH, package_prefix="cogs.events")
    await bot.tree.sync()

if __name__ == "__main__":
    bot.run(
        DEFAULT_TOKEN, #type: ignore
        log_handler=None,
        log_level=logging.DEBUG,
    )
