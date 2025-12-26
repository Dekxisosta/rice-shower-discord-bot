import os
from discord.ext import commands
from utils.console_logger import log

async def autoload_folder(bot: commands.Bot, folder_path: str, package_prefix: str):
    folder_abs = os.path.abspath(folder_path)
    success_count = 0
    failed_count = 0
    for filename in os.listdir(folder_abs):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            full_path = f"{package_prefix}.{module_name}"
            try:
                await bot.load_extension(full_path)
                log(f"Loaded {full_path}", module_name="AUTOLOADER", success = True)
                success_count += 1
            except Exception as e:
                log(f"Failed to load {full_path}: {e}", module_name="AUTOLOADER", success = False)
                failed_count += 1

    log(f"Successfully loaded {success_count}/{(success_count+failed_count)} cogs from {package_prefix}.", module_name="AUTOLOADER", success = True)