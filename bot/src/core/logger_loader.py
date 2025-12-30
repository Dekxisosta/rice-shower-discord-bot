import logging
from utils.console_logger import log
import log.file_logger as file_logger

def load():
    try:
        discord_logger = file_logger.setup_logger(logging.DEBUG)
        logging.getLogger("discord").handlers = discord_logger.handlers
        logging.getLogger("discord").setLevel(logging.DEBUG) 
        log("Discord.py logger successfully configured", module_name="LOGGER_SETUP", success=True)
    except Exception as e:
        log(f"Failed to configure Discord.py logger: {e}", module_name="LOGGER_SETUP", success=False)