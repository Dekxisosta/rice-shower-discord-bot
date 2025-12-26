import yaml
import logging
import os

with open("config/file_paths.yaml", "r") as file_paths:
    data = yaml.safe_load(file_paths)

LOGGING_FILE_PATH = file_paths["logging"]

os.makedirs(os.path.dirname(LOGGING_FILE_PATH), exist_ok=True)

def setup_logger(level=logging.DEBUG):
    logger = logging.getLogger()
    if not logger.hasHandlers():
        logger.setLevel(level)
        logger.addHandler(_setup_file_handler(LOGGING_FILE_PATH))
    return logger

def _setup_file_handler(log_file):
    file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="a")
    file_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    return file_handler
