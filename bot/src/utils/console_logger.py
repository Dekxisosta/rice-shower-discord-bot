from datetime import datetime
from bot.src.config.system_details import SYSTEM_NAME

def log(message: str, module_name: str = "N/A", success: bool = True):
    now = datetime.now()
    if success:
        print(f"🥕 {now} | INFO | {SYSTEM_NAME}:{module_name} | {message}")
    else:
        print(f"🔴 {now} | WARN | {SYSTEM_NAME}:{module_name} | \033[38;5;208m{message}\033[0m")