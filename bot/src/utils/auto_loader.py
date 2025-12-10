import os
from utils import console_logger
from discord.ext import commands

async def autoload_folder(bot: commands.Bot, folder_path: str, package_prefix: str):
    folder_abs = os.path.abspath(folder_path)
    for filename in os.listdir(folder_abs):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            full_path = f"{package_prefix}.{module_name}"
            try:
                await bot.load_extension(full_path)
                console_logger.log(f"Loaded {full_path}", module_name="AUTOLOADER", success = True)
            except Exception as e:
                console_logger.log(f"Failed to load {full_path}: {e}", module_name="AUTOLOADER", success = False)