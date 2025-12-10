from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # two levels up from constants.py

LOGGING_FILE_PATH = BASE_DIR / "log" / "discord.log"
COMMANDS_FOLDER_PATH = BASE_DIR / "cogs" / "commands"
EVENTS_FOLDER_PATH = BASE_DIR / "cogs" / "events"