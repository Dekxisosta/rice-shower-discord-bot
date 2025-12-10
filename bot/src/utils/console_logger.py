from datetime import datetime
from config.constants.system import SYSTEM_NAME

def log(message: str, module_name: str = "N/A", success: bool = True):
    now = datetime.now()
    status_icon = "🥕" if success else "⚠️"
    print(f"[{now}]=====-----++++\n{status_icon} [{SYSTEM_NAME}:{module_name}] {message}\n")